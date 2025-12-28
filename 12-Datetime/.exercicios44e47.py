'''A44: 
Exercício 1 – Relógio de verificação

Mostre a hora atual no terminal, mas com a seguinte regra:

    Se a hora for antes das 12h, imprima: "Bom dia!"

    Se estiver entre 12h e 18h: "Boa tarde!"

    Depois disso: "Boa noite!"

Exercício 2 – Quantos meses faltam?

    Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

        Hoje é o 4º mês do ano. Ainda faltam 8 meses para terminar o ano!

Exercício 3 – Assinatura digital do terminal

    Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:

        Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02

    A data e horário devem ser do momento atual da assinatura'''

# A45:
from datetime import datetime

# Exercício 1 – Relógio de verificação
hora = datetime.now().hour
if hora < 12:
    print(f'Bom dia! Agora são: {hora}h')
elif 12 <= hora < 18:
    print(f'Boa tarde! Agora são: {hora}h')
else:
    print(f'Boa noite! Agora são: {hora}h')

# Exercício 2 – Quantos meses faltam?
mes = datetime.now().month
if mes == 12:
    print(f'Estamos em Dezembro({mes}), último mês do ano!')
else:
    print(f'Estamos no mês {mes}, faltam {mes-12} meses para acabar o ano!')

# Exercício 3 – Assinatura digital do terminal
def assinatura(nome):
    print(datetime.now().strftime(f'Assinatura gerada por {nome} em %d de %h de %Y às %H:%M'))

nome = 'Drew'
#input('Digite seu nome: ')
assinatura(nome)


'''A47:
Exercício 1 – Contagem regressiva para o fim do ano

    Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

Exercício 2 – Verificador de evento

    Peça ao usuário que digite uma data de um evento

    Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

Exercício 3 – Validade de produto 🥫

Peça ao usuário para informar a data de fabricação de um produto.
Considere que ele vence em 180 dias.
Mostre:

    A data de validade

    Se o produto ainda está válido ou já venceu

    Quantos dias faltam ou há quanto tempo passou do prazo'''

# A48:
from datetime import timedelta

# Exercício 1 – Contagem regressiva para o fim do ano
agora = datetime.now()
ano = f'31/12/{agora.year}'
fim_ano = datetime.strptime(ano, '%d/%m/%Y')
hoje = agora.strftime('%d/%m/%Y')
dia = datetime.strptime(hoje, '%d/%m/%Y')
cont = f'{fim_ano - dia}'
print(f'Faltam {cont[:3].strip(' d')} dias para o fim do ano.')

# Gabarito:
hoje = datetime.now()
fim_do_ano = datetime(hoje.year, 12, 31)

dias_restantes = fim_do_ano - hoje
dias_restantes = dias_restantes.days

print(f"Faltam {dias_restantes} dias para o dia 31 de dezembro.")

# Exercício 2 – Verificador de evento
evento = input('Infome a data do evento (dia/mês/ano): ')
evento = datetime.strptime(evento, '%d/%m/%Y')
hoje = datetime.now()

if evento.date() == hoje.date(): #.date() substitui a nececidade do .month + .day
    print("Hoje é o dia do evento!")
elif evento > hoje:
    print("O evento ainda vai acontecer!")
elif evento < hoje:
    print("Já passou o evento!")

# Exercício 3 – Validade de produto 🥫
hoje = datetime.now()
val = timedelta(days=180)
fab = input('Infome a data de fabricação (dia/mês/ano): ')
fab = datetime.strptime(fab, '%d/%m/%Y')

venc = fab + val
print(f'Data de validade: {venc.strftime('%d/%m/%Y')}')

prazo = venc - hoje
if venc > hoje:
    print(f'Seu produto vence em: {prazo.days+1} dias.')
else:
    print(f'Seu produto venceu há: {prazo.days+1} dias.')
