'''Análise de um relatório PDF de vendas

Descrição do PDF:

Abra o pdf vendas.pdf
É um relatório fictício com 5 páginas, cada página contém o nome da loja, a data do relatório e a lista de produtos vendidos com suas quantidades. Alguns produtos aparecem em várias páginas. As datas estão no formato dd/mm/aaaa.

Exemplo de texto dentro de uma página:

    Relatório de Vendas - Loja Alpha  
    Data: 01/07/2025
     
    Produtos vendidos:  
    Teclado: 10 unidades  
    Mouse: 15 unidades  
    Monitor: 5 unidades  
    Impressora: 2 unidades  

Etapas do exercício

    Abrir o arquivo e imprimir o número total de páginas.

    Juntar o texto de todas as páginas em uma string única.

    Criar uma função que receba o texto completo e retorne uma lista com todas as datas encontradas no relatório, no formato dd/mm/aaaa.

    Criar uma função que, dada uma lista de produtos (exemplo: ["Mouse", "Monitor"]) e o texto completo, retorne a soma total de unidades vendidas para cada produto, considerando todas as páginas.

        Exemplo de saída:

            Mouse: 72 unidades  
            Monitor: 31 unidades  

    Gerar um arquivo de texto resumo_vendas.txt contendo um relatório simples, listando os produtos com suas quantidades totais vendidas e as datas de relatório encontradas.'''

from rich import print
from rich.traceback import install
install()
# Abrir o arquivo e imprimir o número total de páginas.
from pypdf import PdfReader

pdf = PdfReader('vendas.pdf')
print('N° de páginas:', len(pdf.pages), '\n')

# Juntar o texto de todas as páginas em uma string única.
string = ''
for pagina in pdf.pages:
    print(pagina.extract_text())
    string += pagina.extract_text()

#print(string)

# Criar uma função que receba o texto completo e retorne uma lista com todas as datas encontradas no relatório, no formato dd/mm/aaaa.

def data(x):
    datas = []
    for linha in x.splitlines():
        if linha[:4].upper() == 'DATA':            
            datas.append(linha[6:])
    return datas

data(string)

# Criar uma função que, dada uma lista de produtos (exemplo: ["Mouse", "Monitor"]) e o texto completo, retorne a soma total de unidades vendidas para cada produto, considerando todas as páginas.

# Gabarito:
import re

def retornar_vendas(produtos:list, texto:str):
    vendas = {}
    for produto in produtos:
        expressao = rf"({produto}):\s*(\d+)\s*unidades"
        resultados = re.findall(expressao, texto)
        if resultados:
            soma = 0
            for resultado in resultados:
                soma += int(resultado[1])
            vendas[produto] = soma
    
    return vendas

# Gerar um arquivo de texto resumo_vendas.txt contendo um relatório simples, listando os produtos com suas quantidades totais vendidas e as datas de relatório encontradas.

with open('resumo_vendas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'Datas: {data(string)}')
    
# Gabarito:

with open("resumo_vendas.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("RELATÓRIO DE VENDAS\n")
    arquivo.write("="*30)
    arquivo.write('\n')

    arquivo.write("DATAS ENCONTRADAS:\n")
    for dia in data(string):
        arquivo.write(f"{dia}\n")
    
    lista_produtos = ['Mouse', 'Teclado'] # Expressão 
    produtos = retornar_vendas(lista_produtos, string)

    arquivo.write("\nPRODUTOS:\n")

    for produto, qtd in produtos.items():
        arquivo.write(f"{produto}: {qtd}\n")

''' Gabarito:
import re
from pypdf import PdfReader

def retornar_datas(texto:str):
    datas = []
    expressao = r"\d{2}/\d{2}/\d{4}"
    resultados = re.findall(expressao, texto)
    if resultados:
        for resultado in resultados:
            datas.append(resultado)
    return datas

def retornar_vendas(produtos:list, texto:str):
    vendas = {}
    for produto in produtos:
        expressao = rf"({produto}):\s*(\d+)\s*unidades"
        resultados = re.findall(expressao, texto)
        if resultados:
            soma = 0
            for resultado in resultados:
                soma += int(resultado[1])
            vendas[produto] = soma
    
    return vendas

vendas_relatorio = PdfReader("vendas.pdf")
print(f"Número de páginas: {len(vendas_relatorio.pages)}")

texto_completo = ""
for pagina in vendas_relatorio.pages:
    texto_completo += pagina.extract_text()

with open("resumo_vendas.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("RELATÓRIO DE VENDAS\n")
    arquivo.write("="*30)
    arquivo.write('\n')

    arquivo.write("DATAS ENCONTRADAS:\n")
    for data in retornar_datas(texto_completo):
        arquivo.write(f"{data}\n")
    
    lista_produtos = ['Mouse', 'Teclado']
    produtos = retornar_vendas(lista_produtos, texto_completo)

    arquivo.write("\nPRODUTOS:\n")

    for produto, qtd in produtos.items():
        arquivo.write(f"{produto}: {qtd}\n")'''
    