"""Onde esta o Chromium.

Modulo separado de proposito: importar `build_pdf.py` gera o PDF inteiro, e
quem so' quer saber se existe navegador nao pode pagar isso. Assim o gerador e
a conferencia usam a MESMA busca -- duas listas do que conta como navegador
divergiriam no primeiro ajuste.
"""

import os
import pathlib
import shutil
import sys

# Procura um Chromium; nao achando, para e diz o que falta -- nunca segue
# calado deixando um PDF velho no lugar (regra 10b: falhar fechada).
def achar_chrome():
    if os.environ.get('CHROME'):
        return os.environ['CHROME']
    for nome in ('chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable'):
        achado = shutil.which(nome)
        if achado:
            return achado
    for padrao in ('/opt/pw-browsers/chromium-*/chrome-linux/chrome',
                   '/opt/pw-browsers/chromium'):
        for achado in sorted(pathlib.Path('/').glob(padrao.lstrip('/')), reverse=True):
            if os.access(achado, os.X_OK):
                return str(achado)
    sys.exit('Nao achei o Chromium para gerar o PDF. Instale o Chrome ou o Chromium, '
             'ou aponte a variavel CHROME para o executavel.')
