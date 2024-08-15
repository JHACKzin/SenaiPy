import random
print ("Bem-vindo ao jogo de adivinhação!")
print ("Tente adivinhar o número que estou pensando entre 1 e 20.")
print ("Digite 'sair' para encerrar o jogo a qualquer momento.")
numero = random.randint(1,20)
while True:
   palpite = int(input("qual o seu palpite?: "))
   if palpite == numero:
     print ("cagadoooo!!!")
     break
   elif palpite < numero:
      print ("errou tente novamente,chutou baixo...")
   else:
      print ("errou tente novamente,chutou alto...")