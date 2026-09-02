#!/usr/bin/env python3
"""Conferencia do Projeto Azambuja.

Este repositorio nao tem codigo de producao: o entregavel e' documentacao, e o
PDF gerado a partir dela. A regra 11c diz que arquivo gerado so' esta pronto
quando um leitor de terceiro abre -- o proprio gerador dizendo "gerou" nao prova
nada. Ja' aconteceu neste projeto: o gerador trazia caminho absoluto escrito a
mao e morria em qualquer clone que nao fosse o da maquina onde foi escrito, e
nada avisava.

O que ela confere:
  1. todo link interno nos .md aponta para arquivo que existe;
  2. toda lista de markdown tem linha em branco antes (o GitHub tolera, o
     conversor de PDF cola a lista no paragrafo anterior);
  3. o gerador roda de ponta a ponta, num destino descartavel, e o `pypdf` --
     leitor de terceiro, que nao e' quem escreveu o PDF -- abre o resultado,
     conta as paginas e extrai texto.

O que ela NAO cobre, declarado: o conteudo dos documentos. Ela nao le a minuta,
nao confere numero, preco nem prazo. Isso continua sendo leitura humana.

Falha fechada: sem `markdown`, sem Chromium, sem `pypdf`, ela bloqueia e diz o
que falta -- nunca passa dizendo que esta tudo bem quando nao conferiu nada.

Uso:  python3 tools/conferir.py
      python3 tools/conferir.py --autoteste
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Fora do repositorio, ou nao e' arquivo: nao e' problema desta conferencia.
EXTERNO = re.compile(r'^(https?:|mailto:|tel:|#|//)')
LINK = re.compile(r'\[[^\]]*\]\(([^)\s]+)')
ITEM_DE_LISTA = re.compile(r'^\s*(?:[-*+]\s|\d+\.\s)')


# Os documentos que viram PDF, mais os READMEs. `.claude/` fica de fora de
# proposito: a skill de la' e' copia de `danilodme-rgb/instrucoes`, e nao se
# edita aqui -- reclamar dela seria cobrar uma correcao que nao pode ser feita
# neste repositorio.
def markdowns(raiz):
    achados = sorted((raiz / 'docs').rglob('*.md'))
    for extra in ('README.md', 'tools/README.md'):
        if (raiz / extra).exists():
            achados.append(raiz / extra)
    return achados


# So' o que entra no PDF: a armadilha e' do conversor.
def vai_para_o_pdf(arquivo, raiz):
    return arquivo.parent == raiz / 'docs'


def conferir(raiz, problemas):
    """Preenche `problemas` e devolve quantos casos EXECUTARAM, por categoria.

    Contar o que executou, e nao so' o que falhou, e' o que distingue "esta
    tudo certo" de "nada chegou a ser conferido".
    """
    contagem = {'links': 0, 'listas': 0, 'pdf': 0}
    arquivos = markdowns(raiz)

    for arquivo in arquivos:
        rel = arquivo.relative_to(raiz)
        linhas = arquivo.read_text(encoding='utf-8').split('\n')

        dentro_de_bloco = False
        anterior = ''
        for numero, linha in enumerate(linhas, 1):
            if linha.lstrip().startswith('```'):
                dentro_de_bloco = not dentro_de_bloco
                anterior = linha
                continue
            if dentro_de_bloco:
                anterior = linha
                continue

            for alvo in LINK.findall(linha):
                if EXTERNO.match(alvo):
                    continue
                contagem['links'] += 1
                caminho = alvo.split('#')[0]
                if caminho and not (arquivo.parent / caminho).exists():
                    problemas.append(f'{rel}:{numero}: link para "{alvo}", que nao existe')

            # Lista colada no paragrafo anterior. Item depois de item e' a
            # propria lista seguindo; o que quebra o PDF e' o primeiro item
            # logo abaixo de texto corrido.
            if ITEM_DE_LISTA.match(linha) and vai_para_o_pdf(arquivo, raiz):
                contagem['listas'] += 1
                if (anterior.strip()
                        and not ITEM_DE_LISTA.match(anterior)
                        and not anterior.startswith((' ', '\t'))   # continuacao de um item acima
                        and not anterior.lstrip().startswith(('#', '>', '|'))
                        and not anterior.rstrip().endswith(('  ', '\\'))):
                    problemas.append(
                        f'{rel}:{numero}: lista sem linha em branco antes '
                        f'(o conversor de PDF cola ela no paragrafo acima)'
                    )
            anterior = linha

    # ---- o gerador e o leitor de terceiro ----
    contagem['pdf'] += 1
    destino = Path(tempfile.mkdtemp(prefix='conferir-pdf-')) / 'minuta.pdf'
    ambiente = dict(os.environ, SAIDA=str(destino))
    r = subprocess.run([sys.executable, str(raiz / 'tools' / 'build_pdf.py')],
                       capture_output=True, text=True, env=ambiente, cwd=raiz, timeout=600)
    if r.returncode != 0:
        problemas.append('o gerador do PDF falhou:\n      ' +
                         (r.stderr or r.stdout).strip().replace('\n', '\n      ')[-800:])
    elif not destino.exists():
        problemas.append('o gerador saiu com sucesso e nao deixou PDF nenhum')
    else:
        from pypdf import PdfReader
        try:
            leitor = PdfReader(str(destino))
            paginas = len(leitor.pages)
            texto = (leitor.pages[0].extract_text() or '').strip()
        except Exception as e:
            problemas.append(f'o `pypdf` nao conseguiu abrir o PDF gerado: {type(e).__name__}: {e}')
        else:
            if paginas < 10:
                problemas.append(f'o PDF gerado tem {paginas} pagina(s) -- a minuta tem dezenas')
            if len(texto) < 20:
                problemas.append('a primeira pagina do PDF nao tem texto extraivel '
                                 '(fonte quebrada ou pagina em branco)')
            else:
                print(f'  PDF: {paginas} paginas, o `pypdf` abriu e leu a capa.')
    shutil.rmtree(destino.parent, ignore_errors=True)

    return contagem


def exigir_dependencias():
    """Falha fechada: o que falta e' dito, nao contornado."""
    faltando = []
    try:
        import markdown  # noqa: F401
    except ImportError:
        faltando.append('o modulo `markdown` (pip install markdown)')
    try:
        import pypdf  # noqa: F401
    except ImportError:
        faltando.append('o modulo `pypdf` (pip install pypdf), que e o leitor de terceiro')
    # Quem sabe achar o navegador e' o gerador. Repetir a busca aqui criaria
    # duas definicoes de "existe navegador", que divergem no primeiro ajuste.
    r = subprocess.run(
        [sys.executable, '-c',
         'import sys; sys.path.insert(0, %r); '
         'from build_pdf_navegador import achar_chrome; print(achar_chrome())'
         % str(RAIZ / 'tools')],
        capture_output=True, text=True)
    if r.returncode != 0:
        faltando.append('um Chromium ou Chrome instalado (o gerador nao achou nenhum)')
    else:
        print(f'  navegador: {r.stdout.strip()}')
    if faltando:
        print('Nao consigo conferir. Falta:\n')
        for f in faltando:
            print('  - ' + f)
        print('\nSem isso eu nao sei se esta certo -- e "nao sei" nao e "esta tudo bem".')
        sys.exit(1)


def autoteste():
    """Passar nao prova que detecta falha: cada sabotagem tem de reprovar."""
    sabotagens = [
        ('docs/minuta-projeto.md',
         lambda t: t + '\n\nVeja o [anexo que nao existe](anexo-z-inventado.md).\n',
         'link para arquivo que nao existe'),
        ('docs/anexo-b-textos-app.md',
         lambda t: t + '\nUm paragrafo colado na lista:\n- primeiro item\n- segundo item\n',
         'lista sem linha em branco antes'),
        ('tools/build_pdf.py',
         lambda t: t.replace("RAIZ = pathlib.Path(__file__).resolve().parent.parent",
                             "RAIZ = pathlib.Path('/lugar/que/nao/existe')"),
         'gerador que nao acha os documentos'),
    ]
    falhas = 0
    for alvo, sabotar, descricao in sabotagens:
        caixa = Path(tempfile.mkdtemp(prefix='conferir-'))
        try:
            destino = caixa / 'repo'
            shutil.copytree(RAIZ, destino, ignore=shutil.ignore_patterns('.git'))
            arquivo = destino / alvo
            arquivo.write_text(sabotar(arquivo.read_text(encoding='utf-8')), encoding='utf-8')
            problemas = []
            try:
                conferir(destino, problemas)
            except Exception as e:
                problemas.append(f'{type(e).__name__}: {e}')
            if problemas:
                print(f'  ok {descricao}: reprovado, como tem de ser')
            else:
                print(f'  X {descricao}: a conferencia PASSOU numa copia sabotada')
                falhas += 1
        finally:
            shutil.rmtree(caixa, ignore_errors=True)
    if falhas:
        print(f'\nAUTOTESTE REPROVADO: {falhas} sabotagem(ns) passaram batido. '
              f'A conferencia nao confere.')
        sys.exit(1)
    print(f'\nAutoteste: as {len(sabotagens)} sabotagens foram todas pegas.\n')


def main():
    exigir_dependencias()
    if '--autoteste' in sys.argv:
        autoteste()

    problemas = []
    contagem = conferir(RAIZ, problemas)

    # Resultado vazio nao e' prova de ausencia: categoria que nao achou nada
    # significa que a conferencia nao rodou, nao que esta tudo certo.
    minimos = {'links': 5, 'listas': 20, 'pdf': 1}
    for nome, minimo in minimos.items():
        if contagem[nome] < minimo:
            problemas.append(
                f'A propria conferencia falhou: so {contagem[nome]} caso(s) de "{nome}" '
                f'executaram, o minimo e {minimo}. Documento movido ou pasta renomeada? '
                f'Nada foi conferido.'
            )

    if problemas:
        print('\nA conferencia reprovou:\n')
        for p in problemas:
            print('  - ' + p)
            print()
        print(f'{len(problemas)} problema(s).')
        sys.exit(1)

    print(f'\nConferencia passou: {contagem["links"]} link(s) interno(s), '
          f'{contagem["listas"]} lista(s) e o PDF de ponta a ponta.')


if __name__ == '__main__':
    main()
