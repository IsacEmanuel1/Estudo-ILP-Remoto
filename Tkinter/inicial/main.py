import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

janela = tk.Tk()

#Exibir mensagem
messagebox.showinfo("Sucesso", "Suas informações foram salvas!")

#Pegar informações do usuario
nome = simpledialog.askstring("Indentificação", "Escreva seu nome")

print(nome)

#Pegar um arquivo
arquivo = filedialog.askopenfilename()