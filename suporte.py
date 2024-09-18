import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox, simpledialog
import json
import os

# Arquivo JSON para armazenar os chamados
ARQUIVO_CHAMADOS = 'chamados.json'

# Função para carregar os chamados existentes
def carregar_chamados():
    try:
        with open(ARQUIVO_CHAMADOS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar um novo chamado no arquivo JSON
def salvar_chamados(chamados):
    with open(ARQUIVO_CHAMADOS, 'w') as f:
        json.dump(chamados, f, indent=4)

# Função para gerar o próximo número de chamado
def gerar_numero_chamado():
    chamados = carregar_chamados()
    if chamados:
        ultimo_chamado = chamados[-1]['numero do chamado']
        return ultimo_chamado + 1
    return 1

# Função para salvar o chamado atual
def salvar_chamado():
    nome_cliente = entry_cliente.get()
    tipo_problema = combo_tipo_problema.get()
    descricao = text_descricao.get("1.0", tk.END).strip()
    prioridade = combo_prioridade.get()
    numero_chamado = label_numero_chamado['text']
    data_abertura = label_data_abertura['text']
    
    if not nome_cliente or not tipo_problema or not descricao or not prioridade:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    
    novo_chamado = {
        'numero_chamado': numero_chamado,
        'cliente': nome_cliente,
        'tipo_problema': tipo_problema,
        'descricao': descricao,
        'prioridade': prioridade,
        'data_abertura': data_abertura
    }
    
    chamados = carregar_chamados()
    chamados.append(novo_chamado)
    salvar_chamados(chamados)
    
    messagebox.showinfo("Sucesso", f"Chamado {numero_chamado} salvo com sucesso!")
    novo_chamado_func()

# Função para limpar os campos e preparar para um novo chamado
def novo_chamado_func():
    entry_cliente.delete(0, tk.END)
    combo_tipo_problema.set('')
    text_descricao.delete("1.0", tk.END)
    combo_prioridade.set('')
    label_numero_chamado.config(text=gerar_numero_chamado())
    label_data_abertura.config(text=date.today())

# Função para localizar um chamado pelo número
def localizar_chamado():
    numero_chamado = entry_numero_localizar.get()
    chamados = carregar_chamados()
    
    for chamado in chamados:
        if str(chamado['numero_chamado']) == numero_chamado:
            entry_cliente.delete(0, tk.END)
            entry_cliente.insert(0, chamado['cliente'])
            combo_tipo_problema.set(chamado['tipo_problema'])
            text_descricao.delete("1.0", tk.END)
            text_descricao.insert(tk.END, chamado['descricao'])
            combo_prioridade.set(chamado['prioridade'])
            label_numero_chamado.config(text=chamado['numero_chamado'])
            label_data_abertura.config(text=chamado['data_abertura'])
            return
    
    messagebox.showerror("Erro", f"Chamado {numero_chamado} não encontrado.")

# Função para limpar os campos
def limpar_campos():
    entry_cliente.delete(0, tk.END)
    combo_tipo_problema.delete(0, tk.END)
    text_descricao.delete(0, tk.END)
    entry_cliente.focus()

# funçao para avançar a linha com o botao enter
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

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Suporte Técnico")

# Labels e Entries para os campos
tk.Label(janela, text="Nome do Cliente:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_cliente = tk.Entry(janela)
entry_cliente.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

tk.Label(janela, text="Tipo de Problema:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
combo_tipo_problema = ttk.Combobox(janela, values=["Problema de Rede", "Falha de Software", "Erro de Hardware", "Falhas de Hardware: Problemas com computadores, impressoras, roteadores ou outros dispositivos que não funcionam corretamente.",
    "Problemas de Rede: Questões relacionadas à conectividade de rede, como falta de acesso à internet, rede lenta ou problemas de configuração.",
    "Software com Bugs: Erros e falhas em softwares utilizados pelos clientes, que podem causar mau funcionamento ou perda de dados.",
    "Configuração de Sistemas: Dificuldades na configuração de sistemas operacionais, aplicativos ou redes que não estão funcionando conforme esperado.",
    "Segurança de Dados: Problemas relacionados à proteção de dados, como vulnerabilidades de segurança, vírus e malware.",
    "Perda de Dados: Situações em que dados importantes foram perdidos devido a falhas de sistema, exclusão acidental ou corrupção.",
    "Instalação de Software: Dificuldades na instalação de novos programas ou atualizações de software que não são concluídas com sucesso.",
    "Compatibilidade de Software: Problemas com a compatibilidade entre diferentes programas ou entre software e hardware.",
    "Problemas de Backup: Falhas no processo de backup que impedem a recuperação de dados em caso de problemas.",
    "Problemas de Desempenho: Má performance de sistemas e aplicativos, como lentidão ou travamentos frequentes.",
    "Erros de Configuração de E-mail: Dificuldades na configuração de contas de e-mail, como problemas com servidores de e-mail ou sincronização.",
    "Suporte ao Usuário: Questões relacionadas à assistência e orientação fornecida aos usuários para resolver problemas técnicos.",
    "Problemas com Licenciamento: Questões relacionadas ao gerenciamento e validade das licenças de software.",
    "Problemas de Acesso: Questões relacionadas ao acesso a sistemas ou dados, como senhas esquecidas ou permissões inadequadas.",
    "Integração de Sistemas: Dificuldades na integração de diferentes sistemas ou aplicações para que trabalhem juntos de forma eficaz.",
    "Atualizações de Sistema: Problemas surgidos após a atualização de sistemas operacionais ou aplicativos, como incompatibilidades ou falhas.",
    "Erro de Hardware: Quebra física ou mau funcionamento de dispositivos como discos rígidos, placas de vídeo, etc.",
    "Problemas de Impressão: Questões com impressoras, como falhas de impressão, problemas de conectividade ou qualidade de impressão ruim.",
    "Problemas de Configuração de Rede: Problemas relacionados à configuração de roteadores, switches ou redes locais (LAN).",
    "Suporte Remoto: Dificuldades em fornecer suporte técnico remoto, como problemas de conexão remota ou limitações na resolução de problemas à distância."])
combo_tipo_problema.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

tk.Label(janela, text="Descrição do Problema:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
text_descricao = tk.Text(janela, height=5)
text_descricao.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

tk.Label(janela, text="Prioridade:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
combo_prioridade = ttk.Combobox(janela, values=["Baixa", "Média", "Alta"])
combo_prioridade.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

# Label para exibir o Número do Chamado
tk.Label(janela, text="Número do Chamado:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
label_numero_chamado = tk.Label(janela, text=gerar_numero_chamado(), bg='lightgray')
label_numero_chamado.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

# Label para exibir a Data de Abertura
tk.Label(janela, text="Data de Abertura:").grid(row=5, column=0, padx=10, pady=5, sticky='w')
label_data_abertura = tk.Label(janela, text=date.today(), bg='lightgray')
label_data_abertura.grid(row=5, column=1, padx=10, pady=5, sticky='ew')

# Botão para salvar o chamado
btn_salvar = tk.Button(janela, text="Salvar Chamado", command=salvar_chamado)
btn_salvar.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Botão para criar um novo chamado
btn_novo_chamado = tk.Button(janela, text="Novo Chamado", command=novo_chamado_func)
btn_novo_chamado.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Campo para inserir o número de chamado a localizar
tk.Label(janela, text="Localizar Chamado (Número):").grid(row=8, column=0, padx=10, pady=5, sticky='w')
entry_numero_localizar = tk.Entry(janela)
entry_numero_localizar.grid(row=8, column=1, padx=10, pady=5, sticky='ew')

entry_cliente.bind("<Return>", move_focus)
combo_tipo_problema.bind("<Return>", move_focus)
text_descricao.bind("<Return>", move_focus)
combo_prioridade.bind("<Return>", move_focus)

# Botão para localizar o chamado
btn_localizar = tk.Button(janela, text="Localizar Chamado", command=localizar_chamado)
btn_localizar.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Expande as colunas para ajustar o layout
janela.grid_columnconfigure(1, weight=1)

janela.geometry("800x500")

janela.mainloop()