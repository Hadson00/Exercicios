soma = 0
while True:
    numero = int(input("Digite um numero (ou 0 para encerrar): "))

    if numero == 0:
        break

    soma += numero

print(f"o maior numero digitado e: {soma}")