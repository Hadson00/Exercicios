x = int(input("Digite o valor de x: "))

for n in range(x, 1, -1):
    x = x * (n-1)

print("Resultado é: ", x)