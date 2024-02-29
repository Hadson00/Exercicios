x = int(input("Digite um número: "))

for n in range(x, 1, -1):
    x = x * (n-1)

print("Resultado é: ", x)