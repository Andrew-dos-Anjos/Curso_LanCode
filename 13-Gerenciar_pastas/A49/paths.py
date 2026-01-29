from pathlib import Path

caminho_relativo = Path('file.txt') # Arquivo local
caminho_absoluto = Path(r'/home/andrew/Downloads/Notas.txt') # Arquivo externo

caminho = caminho_relativo.absolute() # "Absolutiza" um caminho relativo

if caminho_relativo.exists(): # Verifica existencia do arquivo
    print('Existe')
else: # Por algum motivo está retornando o else (pelo linux)
    print('Existe nn')

# Para verificar se é pasta ou arquivo:
if caminho.is_file():
    print("É um arquivo!")
elif caminho.is_dir():
    print("É uma pasta!")

nova_pasta = Path("NovaPasta/SubPasta/OutraPasta/boneca_russa.exe") # Criação de pasta(s)
nova_pasta.mkdir(exist_ok = True, parents = True) # (1: Não dá erro se já existir, 2: Mutiplas pastas)

# Deletar arquivos e pastas:
novoarq = Path("newfile.txt")
novapasta = Path("NovaPasta")

novoarq.unlink()
novapasta.rmdir()

# Escrever e extrair textos:
novoarq = Path("newfile.txt")
novoarq.write_text("Alguma frase aí", encoding='utf-8')
texto = novoarq.read_text()
print(texto)

# Listar arquivos de uma pasta:
pasta = Path("pasta")
for arquivo in pasta.iterdir(): # .glob("*.txt") para apenas arq .txt ou outro especifico
    print(arquivo)

# Outros modos de pegar o nome de um arquivo:
print(caminho) # Atalho completo

print(caminho.name) # Nome.extensão

print(caminho.stem) # Apenas nome

print(caminho.suffix) # Apenas extensão

arquivo = Path("novo_arquivo.txt")
arquivo.touch() # Cria um arquivo vazio

# OBS.: Para identificar a localização de um arquivo basta clicar com o botão direito e procurar por localização em propriedades