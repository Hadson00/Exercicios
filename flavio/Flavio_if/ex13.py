x = 1
s = 0
med = 0
cont = 0

while x != 0:
    x = int(input("Digite um número: "))
    if x != 0:
        s = s + x
    else:
        break
    cont = cont + 1
med = s / cont

print("soma = ", s)

print("Média = ", med)