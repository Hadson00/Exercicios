def soma(num1, num2):
    return num1 + num2
def subtração(num1, num2):
    return num1 - num2
def multiplicação(num1, num2):
    return num1 * num2
def divisão(num1, num2):
    return num1 / num2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

print("A soma dos dois numeros será: ", soma(num1, num2))
print("A subtração dos dois numeros será: ", subtração(num1, num2))
print("A multiplicação dos dois numeros será: ", multiplicação(num1, num2))
print("A divisão dos dois nuemros será: ", divisão(num1, num2))