soma = 0
while True:
    n = int(input("Digite um número inteiro (digite 0 para parar): "))
    if n == 0:
        break
    soma += n

print("A soma de todos os números digitados é:", soma)