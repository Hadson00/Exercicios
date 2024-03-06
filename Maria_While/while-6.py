soma = 0
while True:
    n = int(input("Digite um número inteiro (Caso queira parar, digite 0): "))
    if n == 0:
        break
    soma += n

print("A soma é:", soma)