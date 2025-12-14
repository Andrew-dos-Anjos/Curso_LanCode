'''Desafio A119:
Criar tabela usuarios com "nome, idade e email";
Fazer entrar em loop pedindo os dados, encerrando quando o campo "nome" ficar em branco;
Cada novo usuário deve ser inserido automaticamente.

A122:
Mostra usuários em ordem alfabética;
Mostra menores de idade;
Mostra maiores de idade.

A125:
1. Adicione uma nova coluna chamada telefone à tabela usuarios - Tipo: TEXT; Valor padrão: "SEM-TELEFONE" (Faça pelo DB Browser).
2. Adicione essas funcionalidades no menu interativo:
    Opção de editar usuário: ao escolher um ID existente, o programa mostra quais campos podem ser alterados (nome, idade, email, telefone) depois, o usuário escolhe qual campo quer editar e informa o novo valor.
    E a opção de remover um usuário com base no ID informado.
    
A128: - Conceito de relacionamento 1:N (um para muitos): Um usuário → pode ter vários pedidos. Um pedido → pertence a um único usuário
1. Criando tabela pedidos que se conecta com a tabela usuarios através do campo usuario_id.
    Estrutura sugerida: descricao - o nome do pedido (ex: “Notebook Dell”); Valor - o preço do pedido; usuario_id - chave estrangeira (o elo que liga o pedido ao usuário)
2. Novas funcionalidades:
[5] — Adicionar pedido: O programa deve pedir o ID de um usuário existente. Depois, perguntar: Descrição do pedido (ex: “Teclado mecânico”) Valor (ex: 199.90) Em seguida, salvar os dados na tabela pedidos, vinculando ao usuário informado.
[6] — Exibir usuários com seus pedidos, combinando os dados das duas tabelas, de modo que o sistema exiba todos os pedidos de cada usuário.
[7] — Exibir pedidos de um usuário específico: Peça o ID do usuário. Liste apenas os pedidos que pertencem a ele. 
Ex.: Pedidos de Ana: 
1. Notebook Dell - R$3500 
2. Mouse Gamer - R$150
ou "Esse usuário ainda não possui pedidos."
[8] — Remover pedido: O programa deve permitir excluir um pedido com base no seu ID. Antes de apagar, confirme com o usuário: "Tem certeza que deseja remover este pedido (s/n)? "

=Objetivo final=

Ter em mãos um Gerenciador de Usuários em um mini sistema de clientes e pedidos, mostrando como duas tabelas se relacionam de forma inteligente.
'''

import sqlite3

conexao = sqlite3.connect("/home/andrew/Documentos/Projetos/Curso_LanCode/31-BDD_SQL_com_SQLite/curso/meu_banco.db")
cursor = conexao.cursor()

# Minha solução 1:

cursor.execute('''CREATE TABLE IF NOT EXISTS cadastros (
               id INTEGER PRIMARY KEY,
               nome TEXT,
               idade INT NOT NULL,
               email TEXT NOT NULL)''')

#while True:
#    print('=Novo usuário=')
#    nome = input('Insira o nome de usuário: ')
#    if nome == '':
#        cursor.execute('SELECT * FROM cadastros')
#        print(cursor.fetchall())
#        break
#    idade = int(input('Insira idade: '))
#    email = input('Insira o email: ')
#    cursor.execute('INSERT INTO cadastros (nome, idade, email) VALUES (?,?,?)', (nome, idade, email))
#    conexao.commit()

# Resolução A120: Está de acordo com a minha solução XD

'''# Minha solução 2:

cursor.execute('SELECT nome, idade FROM cadastros ORDER BY nome ASC') 
cadastros = cursor.fetchall()

for cadastro in cadastros:
    nome, idade = cadastro
    if idade >= 18:
        print(f'\n=Maiores de idade= \nNome: {nome} \nIdade: {idade} anos')
    else:
        print(f'\n=Menores de idade= \nNome: {nome} \nIdade: {idade} anos')'''

# Resolução A123: O meu funcionou, porem não tinha entendido que o objetivo era criar um menu de opções

def add_usuario():
    while True:
        print('=Novo usuário=')
        nome = input('Insira o nome de usuário (Enter para cancelar): ')
        if nome == '':
            cursor.execute('SELECT * FROM cadastros')
            #print(cursor.fetchall())
            break
        idade = int(input('Insira idade: '))
        email = input('Insira o email: ')
        telefone = input('Insira telefone: ')
        cursor.execute('INSERT INTO cadastros (nome, idade, email, telefone) VALUES (?,?,?,?)', (nome, idade, email, telefone))
        conexao.commit()

def view(opcao=2):
    match opcao:
        case '2':
            filtro = 'ORDER BY nome ASC'
        case '2.1':
            filtro = 'WHERE idade < 18'
        case '2.2':
            filtro = 'WHERE idade >= 18'
    cursor.execute(f'SELECT * FROM cadastros {filtro}')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        id, nome, idade, email, telefone = usuario
        print(f'\nID:    {id} \nNome:  {nome} \nIdade: {idade} \nEmail: {email} \nFone:  {telefone}')

# Minha solução 3: 
# Resolução A126: O meu ficou mais completo

def alterar():
    while True:
        num = input('Informe o ID: ').strip()
        if num.isdigit():
            num = int(num)
            break
    cursor.execute(f'SELECT * FROM cadastros WHERE id = {num}')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        id, nome, idade, email, telefone = usuario
        print(f'ID:    {id} \nNome:  {nome} \nIdade: {idade} \nEmail: {email} \nFone:  {telefone}')
    digito = input('Informe o digito do que deseja alterar: \n[1]Nome \n[2]Idade \n[3]Email  \n[4]Telefone \n>').strip()
    if digito in '1234':
        if digito == '1':
            mudar = 'nome'
        elif digito == '2':
            mudar = 'idade'
        elif digito == '3':
            mudar = 'email'
        elif digito == '4':
            mudar = 'telefone'
        novo = input(f'O que deseja substituir em {mudar}? ')
        cursor.execute(f'UPDATE cadastros SET {mudar} = ? WHERE id = ?', (novo, num))
        conexao.commit()
    else:
        print('Operação cancelada.')
    
def remover():
    while True:
        num = input('Informe o ID (0 para cancelar): ').strip()
        if num.isdigit():
            num = int(num)
            cursor.execute(f'DELETE FROM cadastros WHERE id = ?' (num))
            conexao.commit()
            break

# Resolução A129:
cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos(
               id INTEGER PRIMARY KEY,
               descricao TEXT NOT NULL,
               valor REAL NOT NULL,
               usuario_id INTEGER NOT NULL,
               FOREIGN KEY (usuario_id) REFERENCES usuarios (id))""")

def adicionar_pedido():
    print(f"{'='*20}Adicionar Pedido{'='*20}")
    descricao = input("Digite o item do pedido: ")
    valor = int(input("Digite o valor do pedido: "))
    usuario_id = input("Digite o id do usuário que fez o pedido: ")

    cursor.execute("INSERT INTO pedidos (descricao, valor, usuario_id) VALUES (?, ?, ?)", (descricao, valor, usuario_id))
    print(f"Pedido adicionado com sucesso!\n")
    conexao.commit()

def exibir_pedidos(opcao="6"):
    filtro = ""
    if opcao == "7":
        usuario_id = input("Digite o id do usuário: ")
        filtro = f"WHERE usuario_id = {usuario_id}"
    cursor.execute(f"""
SELECT pedidos.id, pedidos.descricao, pedidos.valor, usuarios.nome FROM pedidos
JOIN usuarios
ON pedidos.usuario_id = usuarios.id {filtro}""")
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        pedido_id, pedido_descricao, pedido_valor, usuario_nome = pedido
        print(f"{pedido_id}. {pedido_descricao} | {pedido_valor}R$ | {usuario_nome}\n")
    print(f"\n")
    
def deletar_pedido():
    pedido_id = input("Qual pedido deseja deletar? (digite o id): ")
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id))
    conexao.commit()
    print("Pedido deletado com sucesso!\n")

while True:
    opcao = input('''===O que deseja fazer?===
[0] Sair
[1] Cadastrar novo usuário
[2] Visualizar usuários cadastrados
    [2.1] Visualizar menores de idade
    [2.2] Visualizar maiores de idade
[3] Editar usuário por ID
[4] Remover usuário por ID
[5] Adicionar Pedido
[6] Exibir Pedidos
[7] Exibir Pedidos de usuário
[8] Deletar Pedido\n>''')
    match opcao:
        case '0':
            print('\nPrograma encerrado.')
            break
        case '1':
            add_usuario()
        case '2' | '2.1' | '2.2':
            view(opcao)
        case '3':
            alterar()
        case '4':
            remover()
        case "5":
            adicionar_pedido()
        case "6":
            exibir_pedidos()
        case "7":
            exibir_pedidos(opcao)
        case "8":
            deletar_pedido()   
