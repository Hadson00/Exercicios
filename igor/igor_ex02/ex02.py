def valores(n):
    x1 = 2
    x2 = 3.0
    s = 0

    while x1 <= num:
        print(x1, x2)
        s = s + (x1/x2)
        x1 = x1 + 1 
        x2 = x2 + 2
    return s

num = float(input('Digite um valor: '))
while num < 0:
    num = float(input('Digite um valor positivo: '))

resultado = valores(num)
print(resultado)