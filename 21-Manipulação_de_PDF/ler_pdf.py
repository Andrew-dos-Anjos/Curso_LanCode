# A84
# pip install pypdf

from pypdf import PdfReader

relatorio = PdfReader('relatorio_de_vendas.pdf')
pag1 = relatorio.pages[0]

texto1 = pag1.extract_text()
print(texto1)
print(texto1[:10])

for pagina in relatorio.pages:
    print(pagina.extract_text())

relatorio.close()
