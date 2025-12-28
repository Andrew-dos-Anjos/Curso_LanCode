from datetime import datetime, timedelta

hoje = datetime.now()
um_dia = timedelta(days=1)

amanha = hoje + um_dia
ontem = hoje - um_dia

agora = datetime.now()
futuro = datetime(2048, 12, 28)
dias_restantes = futuro - agora
print(dias_restantes) #.days para abstrair apenas o num de dias

# No exemplo seguinte, no primeiro if, as condições precisam ser assim para não cair como passado por considerar os instantes como milisegundos.
aniversario = datetime(2025, 12, 25)
hoje = datetime.now()

if aniversario.day == hoje.day and aniversario.month == hoje.month:
    print("Hoje é o dia do aniversário!")
elif aniversario > hoje:
    print("O aniversário ainda vai acontecer!")
elif aniversario < hoje:
    print("Já passou o aniversário!")
