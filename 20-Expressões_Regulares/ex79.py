'''Nota: o \w além de letras também captura números e _

(Tinha esquecido de mencionar isso)

1️⃣ Encontre todos os códigos de produto no formato "ABC-1234"
Texto de exemplo:

    texto = "Códigos disponíveis: ABC-1234, DEF-5678, GHI-0001, jkl-9999"

2️⃣ Substitua todas as placas de carro por "PLACA"
Texto de exemplo:

    texto = "Os carros estacionados são: KDA-2341, JHU-8877 e MNO-0000"

3️⃣ Encontre todos os usuários no formato "@nome_usuario" em um comentário
Texto de exemplo:

    texto = "Obrigado @joaopereira e @maria_silva pela ajuda! Também cito @123julio e @_admin"'''

import re

#1️⃣ Encontre todos os códigos de produto no formato "ABC-1234"

texto = "Códigos disponíveis: ABC-1234, DEF-5678, GHI-0001, jkl-9999"
exp = r'\w+-\d+' # ou \w+-\w+ ou \w{3}-\d{4} ou \w+-\d{4} ...

codigos = re.findall(exp, texto)
print(codigos)

#2️⃣ Substitua todas as placas de carro por "PLACA"

texto = "Os carros estacionados são: KDA-2341, JHU-8877 e MNO-0000"
exp = r'\w{3}-\d+'

placa = re.sub(exp, 'PLACA', texto)
print(placa)

#3️⃣ Encontre todos os usuários no formato "@nome_usuario" em um comentário

texto = "Obrigado @joaopereira e @maria_silva pela ajuda! Também cito @123julio e @_admin"
exp = r'@\w+'

usuario = re.findall(exp, texto)
print(usuario)

# No gabarito a unica diferença foi o uso do laço for inves de printar direto.