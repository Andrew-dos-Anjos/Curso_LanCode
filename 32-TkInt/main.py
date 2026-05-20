import tkinter as tk

janela = tk.Tk() # Para instanciar
janela.title('Window')
janela.geometry('400x300')

tk.Label(janela, text='Primeiro Label!').pack()

janela.mainloop()
