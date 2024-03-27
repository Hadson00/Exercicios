y = int(input("Digite qualquer numero: "))

for n in range(y, 1, -1):
    y = y * (n-1)

print("Resultado: ", y)