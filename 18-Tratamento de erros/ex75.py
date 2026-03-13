'''👉 1️⃣ Conversão segura
Peça ao usuário que informe um número. Converta para inteiro usando try-except e exiba o número convertido ou uma mensagem de erro se a conversão falhar.

👉 2️⃣ Leitura de arquivo
Tente abrir um arquivo chamado relatorio2025.txt e exibir o conteúdo. Trate o erro caso o arquivo não exista.

👉 3️⃣ Lista e índice
Dada a lista ["Python", "Excel", "API"], tente acessar um índice informado pelo usuário. Trate o erro se o índice não existir e mostre uma mensagem amigável.'''

# Meu cód:

try:
    n = int(input('Digite um número: '))
except Exception as erro:
    print('Valor invalido!', erro)


try:
    with open ('relatorio2025.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print('Arquivo não encontrado')


lista = ["Python", "Excel", "API"]
x = int(input('Selecione a opção que deseja pelo NÚMERO correspondente: \n0.Python \n1.Excel \n2.API\n'))
try:
    print(f'Opção selecionada: ', lista[x])
except Exception:
    print(f'Opção "{x}" invalida.')

# Gabarito 3:

lista = ["Python", "Excel", "API"]
try:
    indice = int(input("Digite um índice para acessar um valor: "))
    print(lista[indice])
except ValueError as erro:
    print(f"Valor inválido!")
except IndexError as erro:
    print("Índice inválido!")
