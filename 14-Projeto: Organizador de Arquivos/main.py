#Meu código:
from pathlib import Path
import shutil

shutil.unpack_archive('organizador.zip', 'organizador')
ex = extensao = []
cont = 0

for arquivo in Path('organizador').iterdir():
    if not arquivo.suffix in ex:
        ex.append(arquivo.suffix[1:])
        pasta = Path(f'organizador/Arq{arquivo.suffix}')
        pasta.mkdir(exist_ok = True)
    shutil.move(arquivo, pasta/arquivo.name)
    cont += 1

print(f'Total de arquivos: {cont} \nExtensões: {ex}')

'''#Gabarito:
from pathlib import Path
import shutil
from datetime import datetime

pasta_organizada = Path("arquivos_organizados")
arquivo_log = Path("registro.log")
arquivos_qtd = 0
extensoes_encontradas = []

for arquivo in Path('organizador').iterdir():
    arquivos_qtd+=1
    extensao = arquivo.suffix[1:]
    if extensao not in extensoes_encontradas:
        extensoes_encontradas.append(extensao)

    subpasta = pasta_organizada/extensao
    if not subpasta.exists():
        subpasta.mkdir(exist_ok=True, parents=True)
        
    shutil.copy(arquivo, subpasta/arquivo.name)
    with open(arquivo_log, 'a', encoding='utf-8') as log:
        agora = datetime.now()
        log.write(agora.strftime(f"%d/%m/%Y %H:%M:%S Movido o arquivo {arquivo.name} para a pasta {subpasta}\n"))

print(f"{arquivos_qtd} arquivos organizados com sucesso!")
print("Extensões encontradas:")
for extensao in extensoes_encontradas:
    print(extensao)'''
