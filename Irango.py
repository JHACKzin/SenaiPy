import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def resultado():
    quantidade = int(entryQuantidade.get())
    preco = float(entryPreco.get())
    total = quantidade * preco
    labelValortotal.config(text = f"R$ {total:.2f}")

def move_focus(event):
    # Obtém o widget atual que tem o foco
    current_widget = event.widget
    
    # Obtém todos os widgets em ordem de empilhamento
    widgets = current_widget.master.winfo_children()
    
    # Encontra o índice do widget atual
    try:
        index = widgets.index(current_widget)
    except ValueError:
        index = -1
    
    # Move o foco para o próximo widget
    next_index = (index + 2) % len(widgets)
    next_widget = widgets[next_index]
    
    # Define o foco no próximo widget
    next_widget.focus_set()

# Configuração da janela principal
janela = tk.Tk()
janela.title("SISTEMA IRANGO 1.0 :)")
label = tk.Label(janela, text="Faça seu pedido:", font=("Title", 11))
label.pack()

# Criação dos widgets/label/lbl
labelLanche = tk.Label(janela, text="Lanche")
labelLanche.pack(padx=50, pady=5)

entryLanche = tk.Entry(janela, width=100)
entryLanche.pack(padx=50, pady=5)

labelQuantidade = tk.Label(janela, text="Quantidade")
labelQuantidade.pack(padx=50, pady=5),int

entryQuantidade = tk.Entry(janela, width=100)
entryQuantidade.pack(padx=50, pady=5)

labelPreco = tk.Label(janela, text="Preço")
labelPreco.pack(padx=50, pady=5)

entryPreco = tk.Entry(janela, width=100)
entryPreco.pack(padx=50, pady=5)

labelTotal = tk.Label(janela, text="Total do pedido")
labelTotal.pack(padx=50, pady=5)

labelValortotal = tk.Label(janela, width=100)
labelValortotal.pack(padx=50, pady=5)

# Associa a tecla Enter ao evento de mover o foco
entryLanche.bind("<Return>", move_focus)
entryQuantidade.bind("<Return>", move_focus)
entryPreco.bind("<Return>", move_focus)

buttonSalvar = tk.Button(janela, text="Calcular total" , command= resultado)
buttonSalvar.pack(padx=50, pady=50)

janela.geometry("800x500")
# Executa o loop principal da interface gráfica
janela.mainloop()