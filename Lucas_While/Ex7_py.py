maior_numero = 0

while True:
    numero = int(input("Digite um numero (ou 0 para encerrar): "))

    if numero == 0:
        break

    if numero > maior_numero:
        maior_numero = numero

print(f"o maior numero digitado e: {maior_numero}")