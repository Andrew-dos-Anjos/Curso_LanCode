'''✍️ Exercício 1 — Conversor de moeda

✅ Crie um programa que:

    Pergunte ao usuário um valor em reais (BRL).

    Consulte a API AwesomeAPI:

        https://economia.awesomeapi.com.br/last/USD-BRL

    Mostre na tela o valor convertido em dólar (USD).

    Se a API não responder corretamente, informe o usuário.

✍️ Exercício 2 — Gera link de imagem de cachorro aleatório

✅ Crie um programa que:

    Faça uma requisição na API Dog CEO:

        https://dog.ceo/api/breeds/image/random

    Mostre o link da imagem gerada no terminal.

    Verifique o status_code antes de usar o dado.

✍️ Exercício 3 — Estimador de idade para nome

✅ Crie um programa que:

    Pergunte ao usuário um nome.

    Consulte a API Agify.io:

        https://api.agify.io/?name={nome}

    Mostre na tela a idade média esperada para o nome.

    Exemplo de uso da resposta:

    Se o nome não retornar dados, informe o usuário.'''

import requests
# Parte 1:

real = 10.50 #input('Valor para conversão R$')

apix = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dolar = apix.json()['USDBRL']['high']

def converte():
    cambio = float(real)/float(dolar)
    cifrao = f'{cambio:.2f}'

    return cifrao

if apix.status_code == 200:
    print(f'R${real} equivalem hoje a ${converte()} (USD)')
else:
    erro = apix.status_code
    print(f'Erro "{erro}"')

'''Gabarito:
valor_real = float(input("Digite um valor em R$: "))

resultado = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
if resultado.status_code == 200:
    dolar = float(resultado.json()['USDBRL']['bid'])
    valor_dolar = valor_real / dolar
    print(f"O valor digitado em dólar é {valor_dolar:.2f}")
else:
    print("Não foi possível concluir sua solicitação.")'''

# Parte 2:

apiy = requests.get('https://dog.ceo/api/breeds/image/random')
if apiy.status_code == 200:
    #print(apiy.json())
    png_url = apiy.json()['message']
    print(f"Aqui sua foto de cão: {png_url}")
else:
    erro = apiy.status_code
    print(f'Erro "{erro}"')

'''Gabarito:
resposta = requests.get("https://dog.ceo/api/breeds/image/random")

if resposta.status_code == 200:
    link = resposta.json()['message']
    print(f"Aqui sua imagem de cachorro: {link}")
else:
    print("Não foi possível processar sua solicitação.")'''

# Parte 3:

nome = input('Informe um nome para saber a idade esperada desse nome: ')
apiz = requests.get(f'https://api.agify.io/?name={nome}')
age = apiz.json()['age']

if apiz.status_code == 200:
    print(f'A idade correspondente para o nome "{nome}" é de {age} anos.')
else:
    erro = apiz.status_code
    print(f'Erro "{erro}"')

'''Gabarito:
nome = input("Digite seu nome: ")
api_url = f"https://api.agify.io/?name={nome}"

resposta = requests.get(api_url)
if resposta.status_code == 200:
    idade_media = resposta.json()['age']
    print(f"A idade média do nome {nome} é {idade_media}")
else:
    print("Não foi possível concluir sua solicitação.")'''
