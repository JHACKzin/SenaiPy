print ("sistema de conversão do dolar")
print ("desenvolvido por: Samuel Moreira Da Silva")
print ("Copywrite 2024") 
print ("versao 1.")
while True :
    valorEmdDolar = float(input("valor do produto em dolar: US$ "))
    cotacãododolarhoje = float(input("digite a cotação do dolar: R$ "))
    valorconvertido = valorEmdDolar * cotacãododolarhoje
    print (f"o valor convertido de US$ {valorEmdDolar} são: R$ {valorconvertido}")
    sair = input("deseja converter outro valor? <S/N>:")
    if sair.upper() == "N":
        break
print("agradeço pela visita. volte sempre. :-)")