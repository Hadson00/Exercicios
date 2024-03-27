import math

valor = int(input("Digite um valor: "))

if valor in [1, 2, 3]:
    resultado = valor ** 2
    print(f"O quadrado do valor é: {resultado}")
elif valor in [4, 9]:
    resultado = math.sqrt(valor)
    print(f"A raiz quadrada do valor é: {resultado}")
elif valor in [6, 7, 8]:
    resultado = valor / 9
    print(f"O valor dividido por 9 é: {resultado}")
else:
    print("Valor não corresponde a nenhuma das condições especificadas.")