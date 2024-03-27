soma = 0
quantidade_numero = 0

while True:
    numero = int(input("Digite um numero (ou 0 para encerrar): "))

    if numero == 0:
        break
    soma += numero
    quantidade_numero += 1

if quantidade_numero > 0:
    media = soma / quantidade_numero
    print(f"soma: {soma}, media: {media: .2f}")
    print("nenhum numero inserido.")


    