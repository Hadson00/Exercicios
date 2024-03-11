import math

v = float(input("Digite um valor: "))

if v == 1 or v == 2 or v == 3:
    resultado = v ** 2
    print(f"O valor elevado ao quadrado é: {resultado}")
elif v == 4 or v == 9:
    resultado = math.sqrt(v)
    print(f"A raiz quadrada do valor é: {resultado}")
elif v == 6 or v == 7 or v == 8:
    resultado = v / 9
    print(f"O valor dividido por 9 é: {resultado}")
else:
    print("O valor não corresponde a nenhuma condição.")