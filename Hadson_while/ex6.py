i = True
soma = 0

while i:
    num = int(input("Digite um numero: "))
    soma = soma + num
    if num == 0:
        i = False

print(f"Soma dos números digitados: {soma}")