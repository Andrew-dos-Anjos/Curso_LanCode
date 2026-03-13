# A78

import re 
# Exemplo 1:
texto = 'Eu tenho um cão'
expressao = 'cão'

resultado = re.search(expressao, texto) # re.search = apenas 1

if resultado:
    print(resultado.group())
else:
    print('Expressão não encontrada!')

# Ex 2:
txt = 'Meu número é 9912-5003, do meu amigo é 4002-8922'
exp = r'\d{4}-\d\d\d\d' # O "{4}" é o mesmo que "\d\d\d\d" ***

resultados = re.findall(exp, txt) # re.findall = todos
for r in resultados:
    print(r, end=' | ')

# Ex 3:
t = 'Hoje é 28/02/2026 e amanhã será 01-03-2026'
e = r'\d{2}[/-]\d{2}[/-]\d{4}'

novotexto = re.sub(e, 'xx/xx/xxxx', t) # re.sub: substitui
print(novotexto)

# Ex 4:
t = 'E-mails: drew123@gmail.com - drew123@gmail;com (escrito errado) - gilÇñïй@ɥoʇɯɐıl.com'
e = r'\w+@\w+\.\w+' # O @ refere-se a si mesmo, enquanto o . recebe \ pois considera caracteres gerais

resultados = re.findall(e, t)
for r in resultados:
    print(r)

''' ***
1. Sequências Especiais (Atalhos)
Estes são os "atalhos" mais comuns para tipos de caracteres específicos:

Atalho  |  Descrição    |   Equivalente manual
\w	Letras, números e underline (alfanumérico)	[a-zA-Z0-9_]
\W	Qualquer caractere que não seja alfanumérico	[^a-zA-Z0-9_]
\s	Espaços em branco (espaço, tab, quebra de linha)	[ \t\n\r\f\v]
\S	Qualquer caractere que não seja espaço	[^ \t\n\r\f\v]
\D	Qualquer caractere que não seja um dígito	[^0-9]

2. Âncoras (Posicionamento)
Em vez de buscar um caractere, as âncoras buscam uma posição no texto:

    ^: Início da string (ou início da linha em modo multilinha).
    $: Final da string.
    \b: Fronteira de palavra (o limite entre um caractere \w e um espaço ou pontuação). Útil para buscar palavras exatas como "sol" sem pegar "insolação".

3. Conjuntos Personalizados []
Se os atalhos acima não servirem, você pode criar os seus usando colchetes:

    [aeiou]: Qualquer vogal minúscula.
    [a-z]: Qualquer letra minúscula de 'a' a 'z'.
    [A-Z]: Qualquer letra maiúscula.
    [0-5]: Apenas dígitos de 0 a 5.
    [^0-9]: O símbolo ^ dentro de colchetes significa negação (neste caso, tudo que não for número).

4. Metacaracteres de Controle

    . (Ponto): Corresponde a qualquer caractere, exceto quebra de linha.
    | (Pipe): Funciona como um "OU". Ex: gato|cachorro.
    \ (Escape): Usado para buscar caracteres que têm significado especial. Ex: para buscar um ponto final literal, use \..

Dica: Quantificadores
Para buscar padrões repetidos, usamos estes símbolos logo após o caractere:

    *: 0 ou mais vezes.
    +: 1 ou mais vezes.
    ?: 0 ou 1 vez (opcional).'''

t = 'abcdefghijklmnopqrstuvwxyz0123456789'
e1 = r'\D'
e2 = r'[a-m]'
e3 = r'\d'
print(re.findall(e1, t))
print(re.findall(e2, t))
print(re.findall(e3, t))
