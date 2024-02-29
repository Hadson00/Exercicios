i = int(input("Digite o valor de i: "))
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
if i % 2 == 0:
    m = a + b + c
    m = m / 3
    print("Média dos números a, b e c é igual a",m)
else:
    a = a * 2
    b = b * 3
    c = c * 4
    p = a + b + c
    p = p / 9
    print("Média ponderada dos números a,b e c é igual a",p)