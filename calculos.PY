#one = float(input("digite um numero para a soma: "))
#two = float(input("digite mais um numero para a soma: "))
#print ("sua soma é: ",one + two)
rodar = 'S'
#while rodar == 'S' or rodar == 's' :
while rodar.upper() == 'S' :
    operacao = input("digite 1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão: ")
    if not operacao.isdigit():
       continue
    if int(operacao) >4 or int(operacao)<1:
       continue
    one = float(input("digite um numero: "))
    two = float(input("digite mais um numero: "))
    if operacao == "1":
      resultado = one + two
    elif operacao == "2":
      resultado = one - two
    elif operacao == "3":
      resultado = one * two
    else:
      resultado = one / two
    print ("o resultado é: ", resultado)
    rodar = input("deseja fazer outra conta? <S/N>: ")
    while rodar.upper() != 'S' and rodar.upper() != 'N':
          rodar = input("opcao invalida. digite S ou N-> ")