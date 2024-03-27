x = int(input("Digite um numero inteiro e positivo: "))
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if (x % 2) == 0:
    print((a + b + c) / 3)
elif x > 10:
    print(((a * 2) + (b * 3) + (c * 4)) / 9)
else:
    print("Numero invalido")

    