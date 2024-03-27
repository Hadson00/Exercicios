numero = int(input("Digite um numero: "))

contagem = 0

while numero != 0:
    numero //= 10
    contagem += 1


print(f"o numero digitado foi {numero}, enquanto a contagem e {contagem}")