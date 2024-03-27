def mediana_tres(a, b, c):
    lista = [a, b, c]
    lista.sort()
    return lista[1]


valor1 = float(input("Insira o primeiro número"))
valor2 = float(input("Insira o primeiro número"))
valor3 = float(input("Insira o primeiro número"))


mediana = mediana_tres(valor1, valor2, valor3)
print(f"A medida dos três valores é: {mediana}")