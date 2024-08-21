def adicao(numA, numB):
    return numA+numB

def subtracao(numA, numB):
    return numA-numB

def multiplicacao(numA, numB):
    return numA*numB

def divisao(numA, numB):
    return numA/numB

print("escolha uma opção: ")
print("1 - adição")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
opcao = input("digite a opção desejada: ")
rodar = 'S'
#while rodar == 'S' or rodar == 's' :
while rodar.upper() == 'S' :
 if opcao == "1":
    numeroA = float(input("digite o primeiro número: "))
    numeroB = float(input("digite o segundo número: "))
    resultado = adicao(numeroA,numeroB)
 elif opcao == "2":
    numeroA = float(input("digite o primeiro número: "))
    numeroB = float(input("digite o segundo número: "))
    resultado = subtracao(numeroA,numeroB)
 elif opcao == "3":
    numeroA = float(input("digite o primeiro número: "))
    numeroB = float(input("digite o segundo número: "))
    resultado = multiplicacao(numeroA,numeroB)
 elif opcao == "4":
    numeroA = float(input("digite o primeiro número: "))
    numeroB = float(input("digite o segundo número: "))
    resultado = divisao(numeroA,numeroB)
 print (f"o resultado é {resultado:.2f} ")
 rodar = input("deseja fazer outra conta? <S/N>: ")
while rodar.upper() != 'S' and rodar.upper() != 'N':
          rodar = input("opcao invalida. digite S ou N-> ")