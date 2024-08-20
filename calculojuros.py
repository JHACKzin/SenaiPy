print ("sistema de calculo de juros")
print ("desenvolvido por: Samuel Moreira Da Silva")
print ("Copywrite 2024") 
print ("versao 1.")
print ("olá estamos aqui para te ajudar a calcular os seus juros:")
while True :
    valordaconta = float(input("qual é o valor da sua conta? R$ "))
    diasdeatraso = int(input("quantos foram os dias de atraso de sua conta? "))
    jurospordia = float(input("qual é o valor do juros por dia?: % "))
    valorcorrigido = valordaconta + (valordaconta*diasdeatraso*(jurospordia/100))
    print (f"o valor do juros mais a conta é: R$ {valorcorrigido:.2F}")
    sair = input("deseja calcular o juros de outra conta? <S/N>:")
    if sair.upper() == "N":
        break
print("Agora vá pagar sua conta por favor... :-)")