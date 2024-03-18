def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número: "))
if par(numero):
    print(numero, "é par.")
else:
    print(numero, "é ímpar.")