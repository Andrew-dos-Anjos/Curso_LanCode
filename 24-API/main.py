# A98
# pip install requests

# API - Application Programming Interface (Interface de Programação de Aplicações)

import requests

cep = '01001000'
url = f'https://viacep.com.br/ws/{cep}/json'

resposta = requests.get(url)
if resposta.status_code == 200: # Ao retornar 200 de status da requisição, significa que obteve êxito
    print(resposta.json()) #['estado'])  # Retorna "São Paulo"
else:
    print(resposta.status_code)


resposta = requests.get("https://api.thecatapi.com/v1/images/search")
if resposta.status_code == 200:
    print(resposta.json())
    gato_url = resposta.json()[0]['url'] # Aqui não basta apenas procurar por 'url' por ser uma lista dentro do dicionário, sendo uma lista só o argumento inicial para retratar-la precisa ser [0]
    print(f"Aqui sua foto de gato: {gato_url}")
