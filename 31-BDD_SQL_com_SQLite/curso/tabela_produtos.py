'''Arquivo "00" é de uma aula do YouTube. Neste módulo (A117) é mostrado os comandos de BDD (SQL) pelo DB Browser e em paralelo os mesmos em python pelo SQLite3'''

import sqlite3

# Importante definir o caminho completo para não ficar a executar em outro lugar:
conexao = sqlite3.connect("/home/andrew/Documentos/Projetos/Curso_LanCode/31-BDD_SQL_com_SQLite/curso/meu_banco.db")
cursor = conexao.cursor()

cursor.execute('DROP TABLE IF EXISTS produtos') # Apaga a tabela!
#cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
#               id INTEGER PRIMARY KEY,
#               nome TEXT NOT NULL,
#               preco REAL NOT NULL)''')

# Inserção de valores:
'''produto_nome = input('Insira um novo produto: ')
produto_preco = float(input(f'Qual o preço de {produto_nome}? R$'))

# Sujeito a ataques de injeção SQL:
#cursor.execute(f'INSERT INTO produtos (nome, preco) VALUES ("{produto_nome}", {produto_preco})')
# Forma adequada:
cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?,?)', (produto_nome, produto_preco))'''

# A121: 
#cursor.execute('SELECT * FROM produtos WHERE preco < ?', ('5')) 
produtos = cursor.fetchall()

print(produtos)
for produto in produtos:
    id, nome, preco = produto
    print(f'\nCódigo: {id} \nNome: {nome} \nPreço: {preco}')


# A123: (DB Browser)

# UPDATE produtos SET preco = 2.50, nome = "Sabão Líguido" WHERE id = 2;
# UPDATE produtos
# SET preco = 10
# WHERE ID = 3;
# 
# DELETE FROM produtos WHERE id = 1
# 
# ALTER TABLE produtos
# ADD COLUMN estoque INTEGER NOT NULL DEFAULT 0;
# RENAME COLUMN estoque TO em_estoque;
# DROP em_estoque;

# A127: 
# Para relacionar tabelas pelo SQLite, é necessário parametrizar tudo na criação, isso é uma limitação exclusiva deste BDD. Nos demais casos basta adicionar uma nova coluna.

cursor.execute('DROP TABLE IF EXISTS categorias')
# Tabela a ser relacionada:
cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL)''')

cursor.execute('''INSERT INTO categorias (nome) VALUES
               ('Alimentos'),
               ('Eletrônicos'),
               ('Móveis')''')

# Recriando tb produtos:
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               preco REAL NOT NULL,
               categoria_id INTEGER,
               FOREIGN KEY (categoria_id) REFERENCES categoria_id (id))''')

cursor.execute('''INSERT INTO produtos (nome, preco, categoria_id) VALUES
               ('Sofá', 900, 3),
               ('Geladeira', 500, 2),
               ('Tomate', 5, 1)''')
cursor.execute('INSERT INTO produtos (nome, preco) VALUES ("Louça", 19.99)')

# Junção das tabelas:
cursor.execute('''SELECT produtos.nome, produtos.preco, categorias.nome AS categoria FROM produtos
LEFT JOIN categorias 
ON produtos.categoria_id = categorias.id''')

produtos = cursor.fetchall()
print(produtos)
for produto in produtos:
    nome, preco, categoria_id = produto
    print(f'\nNome: {nome} \nPreço: R${preco} \nCategoria: {categoria_id}')
conexao.commit()
