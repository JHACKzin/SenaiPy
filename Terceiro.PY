#idade = int(input("qual sua idade? "))
#for contador in range (idade+1):
 #print (contador)

sair = "N"
while sair != "S":
   nome = input("digite um nome: ")
   if nome =="":
     break
   for letra in nome:
     print(letra)
   print("****************")
   sair = input("sair do programa? (S/N): ")