import math
x = int(input("Digite um valor: "))
if x == 1 or x == 2:
    x = x **3
    print(x)
elif (x % 3) == 0:
    print(math.factorial(x))
elif x == 4 or x == 5 or x == 7 or x == 8:
    x = x/9
    print(x)
else:
    print("Valor inválido")