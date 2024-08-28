import tkinter as tk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("Concluido", f"{entryNome.get()};\ntel:{entryTelefone.get()}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("cadastro de cliente")


# Criação dos widgets/label/lbl
labelNome = tk.Label(janela, text="NOME",font=("arial", 12), fg="blue", bg="pink")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela, width=100)
entryNome.pack(padx=50, pady=5)

labelTelefone = tk.Label(janela, text="TELEFONE",font=("arial", 12), fg="blue", bg="pink")
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela, width=100)
entryTelefone.pack(padx=50, pady=5)

labelEmail = tk.Label(janela, text="EMAIL",font=("arial", 12), fg="blue", bg="pink")
labelEmail.pack(padx=50, pady=5)

entryEmail = tk.Entry(janela, width=100)
entryEmail.pack(padx=50, pady=5)

buttonSalvar = tk.Button(janela, text="Salvar",font=("arial", 12), fg="blue", bg="pink", command=mensagem)
buttonSalvar.pack(padx=50, pady=50)

janela.geometry("400x300")
# Executa o loop principal da interface gráfica
janela.mainloop()