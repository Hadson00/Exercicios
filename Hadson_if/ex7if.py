i = int(input("Digite um número: "))
a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))
x = 0
y = 0

if (i % 2) == 0:
    x = x + (a + b + c) / 3
    print(x)
elif i > 10:
    y = ((a * 2) + (b * 3) + (c * 4)) / 9
    print(y)
