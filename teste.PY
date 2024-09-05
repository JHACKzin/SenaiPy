import tkinter as tk

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
    next_index = (index + 1) % len(widgets)
    next_widget = widgets[next_index]
    
    # Define o foco no próximo widget
    next_widget.focus_set()

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Foco")

# Cria vários widgets de entrada (Entry)
entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.pack(padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.pack(padx=10, pady=5)

# Associa a tecla Enter ao evento de mover o foco
entry1.bind("<Return>", move_focus)
entry2.bind("<Return>", move_focus)
entry3.bind("<Return>", move_focus)

# Inicia o loop principal da aplicação
root.mainloop()