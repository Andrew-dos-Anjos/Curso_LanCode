# A81

import re
# Agrupamento:
texto = "Código: PROD-54321"
expressao = r"\w{4}-(\d{5})"

resultado = re.search(expressao, texto)
if resultado:
    print(resultado.group(1)) # Vai mostrar apenas o 54321, pois está agrupado em (\d{5})

# Demonstração do agrupamento em tuplas:
texto = "Meu e-mail é irlan@gmail.com. O email do meu amigo é carlos@gmail.com"
expressao = r"(\w+)@(\w+\.\w+)"

resultados = re.findall(expressao, texto)
if resultados:
    print(resultados)

# ".upper" do re:
texto = "Códigos: PROD-54321 prod-49762"
expressao = r"PROD-(\d{5})"

# re.IGNORECASE é como se fosse o .upper da biblioteca, já o re.DOTALL obriga a expressão a considerar TODOS os caracteres possiveis
resultados = re.findall(expressao, texto, flags=re.IGNORECASE | re.DOTALL)
if resultados:
    print(resultados)
