import tkinter as tk
from tkinter.font import Font

janela = tk.Tk()

janela.title("Sistem de cadastro de Usuario")
janela.geometry("900x600")

#Ciria elemento
titulo = tk.Label(text="Meu APP", font=Font(size=22, weight='bold', family='Arial'))
#Posiciona  elemento na jenela
titulo.pack(pady=(25, 10))


janela.mainloop()