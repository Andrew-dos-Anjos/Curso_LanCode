'''💡 Exercício 1 — Relatório de vendas

Crie um arquivo PDF chamado relatorio.pdf contendo:

    Um título centralizado: Relatório de Vendas — Junho 2025

    Um primeiro parágrafo com o texto:
    As vendas de junho apresentaram um crescimento significativo em relação ao mês anterior, impulsionadas por campanhas promocionais e novos lançamentos.

    Um espaçamento de 8 unidades entre os parágrafos

    Um segundo parágrafo com o texto:
    A previsão para o próximo mês é de continuidade do crescimento, especialmente no setor de tecnologia.

💡 Exercício 2 — Cartaz

Crie um arquivo PDF chamado cartaz.pdf contendo:

    Uma imagem (anexada nos recursos) centralizada com largura de 50 mm

    Um texto abaixo da imagem: Evento Python 2025 — Inscreva-se já!

💡 Exercício 3 — Apresentação

Crie um arquivo PDF chamado apresentacao.pdf contendo:

    Um parágrafo com o texto:
    Bem-vindo ao curso **Python Automático**! Esperamos que você aproveite a jornada de aprendizado.

    Um espaçamento de 6 unidades

    Um segundo parágrafo com o texto:
    Este curso foi preparado para iniciantes em automação com Python.'''

# Gabarito:

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica', size=16)
pdf.cell(0, 10, text='Relatório de Vendas - Junho 2025')
pdf.ln(20)

pdf.set_font('Helvetica', size=12)
pdf.multi_cell(0, 5, text='As vendas de junho apresentaram um crescimento significativo em relação ao mês anterior, impulsionadas por campanhas promocionais e novos lançamentos.')

pdf.ln(8)

pdf.multi_cell(0, 5, text='A previsão para o próximo mês é de continuidade do crescimento, especialmente no setor de tecnologia.')

pdf.output('relatorio.pdf')


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.image('python_banner.png', w=50, x='CENTER')

pdf.set_font('Helvetica', size=16)
pdf.cell(0, 10, text='Evento Python 2025 - Inscreva-se Já!',align='CENTER')

pdf.output('cartaz.pdf')


from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica', size=12)
pdf.multi_cell(0, 5, text="Bem-vindo ao curso **Python Automático**! Esperamos que você aproveite a jornada de aprendizado.", new_x="LMARGIN", new_y="NEXT")

pdf.ln(6)

pdf.multi_cell(0, 5, "Este curso foi preparado para iniciantes em automação com Python.", new_x="LMARGIN", new_y="NEXT")

pdf.output("apresentacao.pdf")
