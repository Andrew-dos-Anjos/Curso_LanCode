import shutil
from pathlib import Path

# O comando copy2 copia, renomeia e preserva metadados do arquivo original:
shutil.copy2('arq.txt', 'backup/arq_backup.txt') # arq original, local de destino.
# Para copiar todos os arquivos de uma pasta para outra:
shutil.copytree('backup', 'backup_do_backup', dirs_exist_ok=True) # (3: Não dá erro se ja existir)

# Mover arquivos:
shutil.move('backup/arq_backup.txt', 'backup_do_backup/arq_original.txt') # Outra opção seria usar o Path criando variáveis dos arquivos desejados e colocando dentro do parenteses.

# Remover pastas:
shutil.rmtree('backup')

# Compactar pasta:
shutil.make_archive('backup_do_backup', 'zip') # (,,3: Renomear)

# Descompactar pasta:
shutil.unpack_archive('backup_do_backup.zip')


arquivos = Path("arquivos")
arquivos_backup = Path("arquivos_backup")

shutil.copytree(arquivos, arquivos_backup)