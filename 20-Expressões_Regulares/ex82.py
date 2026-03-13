'''👉 Exercício 1
Dado o texto:

    texto = "Veículos: CAR-2023, MOTO-2018, BUS-2015"

Crie uma expressão regular que capture:

    O tipo do veículo (CAR, MOTO, BUS) como primeiro grupo

    O ano como segundo grupo

👉 Exercício 2 – Mensagens de sistema
Um log contém mensagens no formato:

    texto = "[INFO] Processo iniciado em 12:45\n[WARNING] Uso de memória alto às 13:05\n[ERROR] Falha crítica às 13:15"

Encontre todas as mensagens com o tipo (INFO, WARNING, ERROR) como grupo 1 e o horário como grupo 2.'''

import re
# Parte 1:
texto = "Veículos: CAR-2023, MOTO-2018, BUS-2015"
exp = r'(\w+)-(\d+)'

veiculos = re.findall(exp, texto)
if veiculos:
    for veiculo in veiculos:
        print(f"Tipo de veículo: {veiculo[0]} \nAno: {veiculo[1]}\n")

# Parte 2:
texto = "[INFO] Processo iniciado em 12:45\n[WARNING] Uso de memória alto às 13:05\n[ERROR] Falha crítica às 13:15"
exp = r'\[(\w+)\].+(\d{2}:\d{2})' # .+ para considerar tudo entre [] e o horario

mensagens = re.findall(exp, texto)
if mensagens:
    for mensagem in mensagens:
        print(f"Natureza do log: {mensagem[0]} \nHora: {mensagem[1]}\n")
