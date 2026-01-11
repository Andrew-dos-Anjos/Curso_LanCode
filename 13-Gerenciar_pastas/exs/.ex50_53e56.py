'''A50:
Exercício 1 – Criando estrutura de pastas

Crie a seguinte estrutura:

    ├──dados/
    │  ├── entrada/
    │  └── saida/
    ├──relatorios/

    Crie todas as pastas em uma única execução do seu código.

Exercício 2 – Criar vários arquivos de exemplo

Dentro da pasta entrada/, crie 3 arquivos vazios:

    dados1.txt

    dados2.txt

    dados3.txt

Exercício 3 – Conferindo e filtrando arquivos .txt

    Liste todos os arquivos .txt dentro de entrada/.

    Imprima apenas o nome do arquivo (sem o caminho completo).'''

# A51:
from pathlib import Path

# Exercício 1 – Criando estrutura de pastas

'''dados_entrada = Path('dados/entrada')
dados_saida = Path('dados/saida')
relatorios = Path('relatorios')

dados_entrada.mkdir(exist_ok = True, parents = True)
dados_saida.mkdir(exist_ok = True, parents = True)
relatorios.mkdir(exist_ok = True, parents = True)

# Exercício 2 – Criar vários arquivos de exemplo

dadosum = Path('dados/entrada/dados1.txt').touch(exist_ok = True)
dadosdois = Path('dados/entrada/dados2.txt').touch(exist_ok = True)
dadostres = Path('dados/entrada/dados3.txt').touch(exist_ok = True)

# Exercício 3 – Conferindo e filtrando arquivos .txt

for file in dados_entrada.glob('*.txt'):
    print(file.name)'''

'''A53:
1. Cópia simples com estrutura

Crie um script que:

    Crie uma pasta imagens.

    Coloque 2 arquivos fictícios .png dentro dela

    Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup.

2. Mover e renomear arquivos automaticamente

Crie um script que:

    Verifica se existe um arquivo chamado relatorio.txt.

    Move esse arquivo para uma pasta chamada relatorios_antigos.

    Durante a movimentação, renomeie o arquivo para relatorio_backup.txt.

3. Automatizando extração de arquivos

Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:

    Crie uma pasta chamada extraido/.

    Extraia o conteúdo do .zip dentro da pasta criada.

    Ao final, liste todos os arquivos extraídos.'''

# A54:
import shutil

# 1. Cópia simples com estrutura

'''imagens = Path("imagens").mkdir(parents=True, exist_ok=True)
imagem = (Path("imagens/img1.png").touch(), Path("imagens/img2.png").touch())
shutil.copytree('imagens', 'imagens_bkp', dirs_exist_ok=True)

# 2. Mover e renomear arquivos automaticamente

relatorio = Path("relatorio.txt")
relatorios_antigos = Path("relatorios_antigos").mkdir(parents=True, exist_ok=True)

shutil.move(relatorio, "relatorios_antigos/relatorio_bkp.txt")

# 3. Automatizando extração de arquivos

shutil.unpack_arc # .glob("*.txt") para apenas arq .txt ou outro especificohive('arquivos_secretos.zip', 'extraido')

extraido = Path('extraido')
for arquivo in extraido.iterdir:
    print(arquivo)'''

'''A56:
Exercício 1 — Criando um relatório simples

    Crie um arquivo chamado relatorio.txt que contenha a frase "Estou aprendendo Python!

    Inclua no final do arquivo a data e hora de criação do arquivo de forma automática

Exercício 2 — Contador de letras

Crie um arquivo chamado mensagem.txt com um parágrafo de texto que você inventar. Depois, escreva um script que conte e exiba quantas letras existem nesse texto.

Exercício 3 — Filtrando logs por palavra-chave

Baixe o arquivo logs.txt anexado, e escreva um programa que:

    Leia todas as linhas do arquivo

    Peça ao usuário uma palavra-chave (ERROR, INFO, WARNING ou DEBUG)

    Mostre apenas as linhas que contenham essa palavra-chave.'''

# A57:
from datetime import datetime

# Exercício 1 — Criando um relatório simples

with open ('relatorio.txt', 'w+', encoding='utf-8') as arquivo:
    arquivo.write(f'Estou aprendendo Python! \nData: {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    arquivo.seek(0)
    print(arquivo.read())

# Exercício 2 — Contador de letras

with open ('mensagem.txt', 'w+', encoding='utf-8') as arquivo:
    print(arquivo.write('cinco'))

# Exercício 3 — Filtrando logs por palavra-chave

while True:
    word = input('Selecione o digito ref. às linhas que deseja visualizar do relatório com a palavra-chave: \n[1] ERROR \n[2] INFO \n[3] WARNING \n[4] DEBUG \n[0] Para cancelar! \n>>')#; print('\n')
    if not word in '01234':
        print(f'\033[31mArgumento não válido! "{word}" \033[m')
        continue
    if word == '0':
                print('Good bye')
                break
    
    with open ('acesso.log', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if word == '1':
                if linha.find('ERROR') != -1:
                    print(linha)
            elif word == '2':
                if linha.find('INFO') != -1:
                    print(linha)
            elif word == '3':
                if linha.find('WARNING') != -1:
                    print(linha)
            elif word == '4':
                if linha.find('DEBUG') != -1:
                    print(linha)

# Gabarito:
with open("acesso.log", encoding="utf-8") as arquivo:
    palavra_chave = input("Qual palavra quer usar?: ")
    for linha in arquivo.readlines():
        if palavra_chave.upper() in linha:
            print(linha)
