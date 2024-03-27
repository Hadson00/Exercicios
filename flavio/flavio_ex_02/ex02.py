def valores(n):
    y1 = 2
    y2 = 3.0
    soma = 0

    while y1 <= num:
        print(y1,y2)
        soma = soma + (y1/y2)
        y1 = y1 + 1 
        y2 = y2 + 2
    return soma

num = float(input("Digite um valor: "))
while num < 0:
    num = float(input("Digite um valor positivo: "))

resul = valores(num)
print(resul)
    