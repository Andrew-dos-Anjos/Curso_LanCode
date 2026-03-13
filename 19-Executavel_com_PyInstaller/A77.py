import os

os.system('msg * "Olá, mundo!"') # Windows
os.system('notify-send "Olá, mundo!" "Esta é uma mensagem de teste"') # Linux

# source .venv/bin/activate  # Linux (cd pasta_exata)
# pip install PyInstaller
# pyinstaller --onefile arquivo.py
# Dist

# pyinstaller --icon=icon.ico arquivo.py
# https://icon-icons.com/search?q=python

# pyinstaller --noconsole arquivo.py (para execultar sem visualizar)
