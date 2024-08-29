import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def mensagem():
    messagebox.showinfo("CADASTRO CONCLUÍDO", f"{entryNometutor.get()};\nPET:{entryNomepet.get()}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("CADASTRO PET SHOP SACOOBY DOOH :)")


# Criação dos widgets/label/lbl
labelNometutor = tk.Label(janela, text="NOME DO TUTOR",font=("arial", 12), fg="blue", bg="pink")
labelNometutor.pack(padx=50, pady=5)

entryNometutor = tk.Entry(janela, width=100)
entryNometutor.pack(padx=50, pady=5)

labelNomepet = tk.Label(janela, text="NOME DO PET",font=("arial", 12), fg="blue", bg="pink")
labelNomepet.pack(padx=50, pady=5)

entryNomepet = tk.Entry(janela, width=100)
entryNomepet.pack(padx=50, pady=5)

labelDatapet = tk.Label(janela, text="DATA DE NASCIMENTO DO PET",font=("arial", 12), fg="blue", bg="pink")
labelDatapet.pack(padx=50, pady=5)

entryDatapet = tk.Entry(janela, width=100)
entryDatapet.pack(padx=50, pady=5)

labelEspeciepet = tk.Label(janela, text="ESPÉCIE DO PET",font=("arial", 12), fg="blue", bg="pink")
labelEspeciepet.pack(padx=50, pady=5)

entryEspeciepet = tk.Entry(janela, width=100)
entryEspeciepet.pack(padx=50, pady=5)

#combobox das especies de pet
comboboxEspecie = ttk.Combobox(entryEspeciepet, values=["Abelhas", "Alpaca", "Bicho-da-seda", "Búfalo", "Cabra", "Cachorro", "Calopsita", "Camelo", "Camundongo", "Canário-do-reino ou canário-belga", "Cavalo", "Chinchila", "Cisne-negro", "Cobaia ou porquinho-da-India", "Codorna-chinesa", "Coelho", "Diamante-de-gould", "Diamante-mandarim", "Dromedário", "Escargot", "Faisão-de-coleira", "Gado bovino", "Gado zebuino", "Galinha", "Galinha-d-angola", "Ganso", "Ganso-canadense", "Ganso-do-nilo", "Gato", "Hamster", "Jumento", "Lhama", "Manon", "Marreco", "Minhoca", "Ovelha", "Pato-carolina", "Pato-mandarim", "Pavão", "Perdiz-chucar", "Periquito-australiano", "Peru", "Phaeton", "Pomba-diamante", "Pombo-doméstico", "Porco", "Ratazana", "Rato", "Tadorna"])
comboboxEspecie.pack(pady=1)
selected_value = comboboxEspecie.get()

labelRacapet = tk.Label(janela, text="RAÇA DO PET",font=("arial", 12), fg="blue", bg="pink")
labelRacapet.pack(padx=50, pady=5)

entryRacapet = tk.Entry(janela, width=100)
entryRacapet.pack(padx=50, pady=5)

#combobox das raças de cada especie dos pets
comboboxRacas = ttk.Combobox(entryRacapet, values=["Abelha jandaíra", "Abelha uruçu", "Abelha uruçu-amarela","Abelha mandaçaia", "Abelha jataí", "Abelha europeia", "Abelha africanizada", 
"Huacaya alpaca",
'bicho da seda',"Bombyx mori",
'bufalo', "Carabao", "Murrah", "Mediterrâneo", "Jafarabad", 
"Cabra", "Cachorro", "Calopsita", "Camelo", "Camundongo", "Canário-do-reino ou canário-belga", "Cavalo", "Chinchila", "Cisne-negro", "Cobaia ou porquinho-da-India", "Codorna-chinesa", "Coelho", "Diamante-de-gould", "Diamante-mandarim", "Dromedário", "Escargot", "Faisão-de-coleira", "Gado bovino", "Gado zebuino", "Galinha", "Galinha-d-angola", "Ganso", "Ganso-canadense", "Ganso-do-nilo", "Gato", "Hamster", "Jumento", "Lhama", "Manon", "Marreco", "Minhoca", "Ovelha", "Pato-carolina", "Pato-mandarim", "Pavão", "Perdiz-chucar", "Periquito-australiano", "Peru", "Phaeton", "Pomba-diamante", "Pombo-doméstico", "Porco", "Ratazana", "Rato", "Tadorna"])
comboboxRacas.pack(pady=1)
selected_value = comboboxRacas.get()

buttonSalvar = tk.Button(janela, text="Salvar",font=("arial", 12), fg="blue", bg="pink", command=mensagem)
buttonSalvar.pack(padx=50, pady=50)

janela.geometry("400x300")
# Executa o loop principal da interface gráfica
janela.mainloop()