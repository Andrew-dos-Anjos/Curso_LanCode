import random

# int_aleatorio = random.randint(1, 100)
# float_aleatorio = random.uniform(0, 1)

# cartas = ['Ás', 'Rei', 'Dama', 'Valete']
# carta_aleatoria = random.choices(cartas, k=2) # k=2: 2 resultados
# carta_aleatoria = random.sample(cartas, k=2) # .sample: Os resultados não serão parecidos

# print(f"Cartas escolhidas: {carta_aleatoria}")

musicas = ['Eletronica', 'Pop', 'Rock', 'Indio']
print(musicas)

random.shuffle(musicas) # Mistura a ordem dos elementos
print(musicas)
