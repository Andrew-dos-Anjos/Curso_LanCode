'''🥇 Exercício — Sorteio de Prêmios em uma Festa

Você está organizando uma festa e tem 5 prêmios diferentes para sortear entre os convidados.

    Cada convidado só pode ganhar um único prêmio.

    Os prêmios também não podem se repetir (obviamente).

    No final, mostre qual convidado ganhou qual prêmio.

Use as seguintes listas:

    convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
    premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]'''

import random
convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

sorteio = random.sample(convidados, k=5)

cont = 0
print('Resultado do sorteio!\n')
for i in premios:
    print(f'{sorteio[cont]} ganhou: {i}')
    cont += 1

# Ou

sorteio2 = random.sample(premios, k=5)

print('\n')
for i in range(5):
    print(f'{sorteio[i]} ganhou: {sorteio2[i]}')
    