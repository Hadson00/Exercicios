a=float(input("Digite um numero: "))
b=float(input("Digite um numero: "))
c=float(input("Digite um numero: "))

if (a < b) and (a > c):
    print(a, " é a mediana!!!!!")
elif (a > b) and (a < c):
    print(a, " é a mediana!!!!!")
elif (b > a) and (b < c):
    print(b, " é a mediana!!!!!")
elif (b < a) and (b > c):
    print(b, " é a mediana!!!!!")
elif (c < a) and (c > b):
    print(c, " é a mediana!!!!!")
elif (c > a) and (c < b):
    print(c, " é a mediana!!!!!")