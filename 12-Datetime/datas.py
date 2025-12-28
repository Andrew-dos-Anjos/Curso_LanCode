'''Aula 43'''
from datetime import datetime

agora = datetime.now()
print(agora)

dia = datetime.now().day
mes = agora.month
ano = agora.year
print(dia, mes, ano)

hora = agora.hour
min = agora.minute
seg = agora.second
mseg = agora.microsecond
print(hora, min, seg, mseg)

data = datetime(2000, 5, 20) # Formatado
print(data.day)

# Cada variável acima está como objeto. O strftime transforma em string
print(agora.strftime("Hoje é dia %d do mês %m do ano %Y \n" \
"Agora são %H horas e %M minutos"))

# E o strptime transforma de volta em objeto
data_str = "27/12/2025"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
print(data_convertida)
