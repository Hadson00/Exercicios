valor = int(input("Digite um valor: "))
if valor < 0: 
    print(valor * -1)
elif valor > 10:
    valor2 = int(input("Digite outro valor: "))
    valor = valor - valor2
    print(valor)
else:
    valor = valor/5
    print(valor)