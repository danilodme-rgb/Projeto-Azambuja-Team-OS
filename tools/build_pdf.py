import re, markdown, subprocess, os, pathlib

DOCS = pathlib.Path('/home/user/Projeto-Azambuja-Team-OS/docs')
fonts = open(pathlib.Path(__file__).parent / 'fonts-embed.css', encoding='utf-8').read()

def render(path):
    md = open(path, encoding='utf-8').read()
    md = md.split('\n', 1)[1] if md.startswith('# ') else md   # tira o H1 (vai na capa)
    md = re.sub(r'~~(.+?)~~', r'<del>\1</del>', md)            # tachado do GitHub
    return markdown.markdown(md, extensions=['tables', 'fenced_code', 'attr_list', 'sane_lists', 'md_in_html'])

corpo   = render(DOCS / 'minuta-projeto.md')
anexo_a = render(DOCS / 'anexo-a-tecnicas-avancadas.md')
anexo_b = render(DOCS / 'anexo-b-textos-app.md')
anexo_c = render(DOCS / 'anexo-c-checklist-reuniao.md')

# --- sumario a partir dos H2 do corpo ---
h2 = re.findall(r'<h2>(.*?)</h2>', corpo)
def slug(t):
    t = re.sub(r'<[^>]+>', '', t)
    return 's-' + re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
for t in h2:
    corpo = corpo.replace('<h2>%s</h2>' % t, '<h2 id="%s">%s</h2>' % (slug(t), t), 1)
sumario = '\n'.join(
    '<li><span class="toc-n">%s</span><span class="toc-t">%s</span></li>' %
    (t.split('.')[0], re.sub(r'<[^>]+>', '', t.split('. ', 1)[1] if '. ' in t else t))
    for t in h2)

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
@page :first { margin: 0; }
""" + fonts + """
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:'Source Serif 4',Charter,Georgia,serif;font-size:10.2pt;line-height:1.55;
  color:#14161c;background:#fff}
h1,h2,h3,h4,th,.k,.cap-t,.toc-t{font-family:Archivo,'Liberation Sans',Arial,sans-serif}
code,.mono,.toc-n{font-family:'IBM Plex Mono','DejaVu Sans Mono',monospace}

/* ---------- capa ---------- */
.cover{height:297mm;padding:26mm 22mm;display:flex;flex-direction:column;
  background:linear-gradient(160deg,#f3f5fa 0%,#fff 55%);page-break-after:always;position:relative}
.cover-k{font-family:'IBM Plex Mono',monospace;font-size:8.5pt;letter-spacing:.22em;
  text-transform:uppercase;color:#1a3cc4;margin-bottom:auto}
.cap-t{font-size:52pt;font-weight:800;letter-spacing:-.035em;line-height:.94;margin:0 0 6mm}
.cap-t em{font-style:normal;color:#1a3cc4;display:block}
.cap-s{font-size:13pt;line-height:1.45;color:#3d4453;max-width:120mm;margin:0 0 12mm}
.cap-bars{display:flex;align-items:flex-end;gap:2.2mm;height:26mm;margin-bottom:12mm}
.cap-bars i{display:block;width:4.4mm;background:#dfe5fb;border-top:1mm solid #1a3cc4}
.cap-meta{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:.4mm solid #14161c;padding-top:5mm}
.cap-meta div{padding-right:5mm}
.cap-meta .k{display:block;font-family:'IBM Plex Mono',monospace;font-size:7pt;letter-spacing:.16em;
  text-transform:uppercase;color:#697285;margin-bottom:1.5mm}
.cap-meta b{font-family:Archivo,sans-serif;font-size:12pt;font-weight:700;letter-spacing:-.02em;display:block}
.cap-meta span.n{font-size:8.5pt;color:#697285;display:block;line-height:1.3}

/* ---------- sumario ---------- */
.toc{page-break-after:always;padding-top:4mm}
.toc h2{border:0;margin:0 0 8mm;padding:0}
.toc ol{list-style:none;padding:0;margin:0;column-count:2;column-gap:12mm}
.toc li{display:flex;gap:4mm;padding:2.1mm 0;border-bottom:.2mm solid #e4e7ee;break-inside:avoid;font-size:9.6pt}
.toc-n{color:#1a3cc4;font-size:8.5pt;min-width:6mm;padding-top:.6mm}
.toc-t{font-weight:600}

/* ---------- tipografia ---------- */
h2{font-size:17pt;font-weight:700;letter-spacing:-.025em;line-height:1.12;
  margin:0 0 4mm;padding-top:5mm;border-top:.6mm solid #14161c;page-break-after:avoid;
  page-break-before:auto;text-wrap:balance}
h3{font-size:11.6pt;font-weight:700;letter-spacing:-.01em;margin:7mm 0 2.5mm;page-break-after:avoid}
h4{font-size:9.6pt;font-weight:700;margin:5mm 0 2mm;page-break-after:avoid}
p{margin:0 0 3mm;orphans:3;widows:3}
ul,ol{margin:0 0 3.5mm;padding-left:6mm}
li{margin-bottom:1.4mm}
strong{font-weight:600}
em{font-style:italic}
hr{border:0;border-top:.2mm solid #d2d7e2;margin:6mm 0}
a{color:#1a3cc4;text-decoration:none}
code{font-size:8.6pt;background:#eef0f5;padding:.4mm 1.2mm;border-radius:.8mm}

blockquote{margin:4mm 0;padding:3mm 0 3mm 5mm;border-left:.8mm solid #1a3cc4;
  background:#f7f8fb;font-size:9.7pt;page-break-inside:avoid}
blockquote p:last-child{margin-bottom:0}

table{width:100%;border-collapse:collapse;font-size:8.8pt;margin:3.5mm 0}
thead{display:table-header-group}
th{text-align:left;font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;color:#697285;
  font-weight:600;padding:2mm 2.5mm;border-bottom:.4mm solid #14161c;background:#f3f5fa}
td{padding:2mm 2.5mm;border-bottom:.2mm solid #e4e7ee;vertical-align:top;line-height:1.4}
td:first-child{font-weight:600}
del{color:#697285}
tr{page-break-inside:avoid}

pre{background:#f3f5fa;border:.2mm solid #e4e7ee;border-radius:1mm;padding:3mm;
  font-size:8.4pt;line-height:1.45;white-space:pre-wrap;word-break:break-word}

.sep{page-break-before:always;padding-top:2mm}
.sep h2{border-top:0;padding-top:0;font-size:22pt}
.sep-k{font-family:'IBM Plex Mono',monospace;font-size:8pt;letter-spacing:.2em;
  text-transform:uppercase;color:#1a3cc4;margin-bottom:3mm}
"""

HTML = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Minuta de Projeto — Azambuja Team OS</title><style>{CSS}</style></head><body>

<div class="cover">
  <div class="cover-k">Minuta de projeto · versão 1.0 · agosto de 2026</div>
  <div class="cap-t">Azambuja<em>Team OS</em></div>
  <p class="cap-s">Plataforma exclusiva de coaching de treino e nutrição: aplicativo para os
  alunos, site de captação e painel administrativo do coach.</p>
  <div class="cap-bars">
    <i style="height:22%"></i><i style="height:34%"></i><i style="height:31%"></i>
    <i style="height:48%"></i><i style="height:57%"></i><i style="height:52%"></i>
    <i style="height:71%"></i><i style="height:84%"></i><i style="height:100%"></i>
  </div>
  <div class="cap-meta">
    <div><span class="k">Prazo do MVP</span><b>10–14</b><span class="n">semanas após congelar o escopo</span></div>
    <div><span class="k">Custo fixo mensal</span><b>R$ 3–15</b><span class="n">um aluno cobre o ano</span></div>
    <div><span class="k">Entregas</span><b>3 produtos</b><span class="n">app, site e painel</span></div>
    <div><span class="k">Fase atual</span><b>Definição</b><span class="n">reunião com o coach</span></div>
  </div>
</div>

<div class="toc"><h2>Sumário</h2><ol>{sumario}</ol></div>

{corpo}

<div class="sep"><div class="sep-k">Anexo A</div><h2>Técnicas avançadas de treino</h2></div>
{anexo_a}
<div class="sep"><div class="sep-k">Anexo B</div><h2>Textos do aplicativo</h2></div>
{anexo_b}
<div class="sep"><div class="sep-k">Anexo C</div><h2>Pauta da reunião de definição</h2></div>
{anexo_c}
</body></html>"""

open('/tmp/minuta-print.html', 'w', encoding='utf-8').write(HTML)

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
out = '/home/user/Projeto-Azambuja-Team-OS/Minuta-Azambuja-Team-OS.pdf'
r = subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
    '--no-pdf-header-footer', '--print-to-pdf=' + out,
    'file://' + '/tmp/minuta-print.html'],
    capture_output=True, text=True, timeout=180)
print('exit', r.returncode, r.stderr[-400:] if r.returncode else '')
print('tamanho KB:', round(os.path.getsize(out) / 1024))
