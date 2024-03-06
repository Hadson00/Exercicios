d = 0
f = 0

for y in range(1, 11):
    x = int(input("Digite um número: "))
    if x >= 10 and x <= 20:
        d = d + 1
    else:
        f = f + 1

print("Números dentro do intervalo: ",d)
print("Números fora do intervalo: ",f)