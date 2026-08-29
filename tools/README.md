# Ferramentas

## `build_pdf.py` — gera o PDF da minuta

Monta um HTML com layout de impressão (A4, capa, sumário automático a partir dos títulos, os
três anexos) a partir dos arquivos de `docs/`, e renderiza com o Chromium headless.

**Dependências:** `pip install markdown` e um Chromium/Chrome disponível.
As fontes (Archivo, Source Serif 4, IBM Plex Mono) são embutidas em `fonts-embed.css` como
data URIs, para o PDF não depender de rede nem das fontes do sistema.

```bash
python3 tools/build_pdf.py
```

Saída: `Minuta-Azambuja-Team-OS.pdf` na raiz do repositório.
