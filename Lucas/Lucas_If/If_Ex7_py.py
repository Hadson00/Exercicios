x = int(input("Digite um número inteiro e positivo: "))
a = int(input("Digite um valor p/a: "))
b = int(input("Digite um valor p/b: "))
c = int(input("Digite um valor p/c: "))

if (x % 2) == 0:
    print((a + b + c) / 3)
elif x > 10:
    print(((a * 2) + (b * 3) + (c * 4)) / 9)