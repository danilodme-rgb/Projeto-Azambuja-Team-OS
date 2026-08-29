# Projeto Azambuja — Team OS

Plataforma exclusiva de coaching de nutrição e treino de musculação: aplicativo iOS/Android
para os alunos + site institucional/captação + painel administrativo para o coach.

> **Status:** Fase 0 — Minuta de projeto para apresentação e validação com o coach.
> Nenhum código de produção foi escrito ainda: a construção começa depois da reunião de
> definição (ver `docs/anexo-c-checklist-reuniao.md`).

## Como trabalhamos

[`CLAUDE.md`](CLAUDE.md) na raiz reúne as instruções de trabalho e é lido automaticamente
no início de toda sessão neste repositório. É o arquivo a copiar para um projeto novo.

## Documentos

| Arquivo | Conteúdo |
|---|---|
| [`docs/minuta-projeto.md`](docs/minuta-projeto.md) | Documento principal: visão, escopo, fluxos, arquitetura, LGPD, custos, cronograma |
| [`docs/anexo-a-tecnicas-avancadas.md`](docs/anexo-a-tecnicas-avancadas.md) | Catálogo de técnicas avançadas de treino — **a definir com o coach** |
| [`docs/anexo-b-textos-app.md`](docs/anexo-b-textos-app.md) | Textos prontos: definições de nível, objetivos, consentimentos LGPD |
| [`docs/anexo-c-checklist-reuniao.md`](docs/anexo-c-checklist-reuniao.md) | Pauta objetiva da reunião, com os códigos das decisões (`A1`, `B3`, `C5`…) |
| [`Minuta-Azambuja-Team-OS.pdf`](Minuta-Azambuja-Team-OS.pdf) | **Versão para apresentação** — minuta + os três anexos, 51 páginas, com capa e sumário |

Para regerar o PDF depois de editar os documentos: `python3 tools/build_pdf.py`

## Próximos passos

1. Revisar a minuta e ajustar o que for necessário.
2. Reunião com o coach usando o Anexo C como pauta.
3. Fechar as **8 decisões do Bloco A** (seção 19.2 da minuta) — são as que travam o início.
4. Congelar o escopo do MVP.
5. Iniciar o desenvolvimento (Fase 1).
