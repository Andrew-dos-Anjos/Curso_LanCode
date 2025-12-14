'''https://youtu.be/YPD0YEjqe90?si=vWdUL0daXvY5xeBQ'''

import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criação do BDD:
cursor.execute('''CREATE TABLE IF NOT EXISTS contas_bancarias (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
               )''')

# Inserção de dados:
#cursor.execute('''INSERT INTO contas_bancarias
#              (titular, saldo, cpf) VALUES
#              ('Guilerme', 3000, '00000000000')
#              ('haglipe', 4.04, '00000000001')''')

# Considera as colunas requisitadas da tabela:
cursor.execute('''SELECT * FROM contas_bancarias
               WHERE id = 1''') # Condicional
contas = cursor.fetchall()
cursor.execute('''DELETE FROM contas_bancarias WHERE id = 4''') # Para deletar 
cursor.execute('''UPDATE contas_bancarias
               SET saldo = 2000000
               WHERE id = 1''') # Para atualizar

print(contas)
for conta in contas:
    id, titular, saldo, cpf = conta
    print(f'\nId: {id} \nTitular: {titular} \nSaldo: {saldo} \nCPF: {cpf}')

conexao.commit() # Salva cada nova alteração no BDD
