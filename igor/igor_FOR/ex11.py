cont = 0
cont2 = 0

for x in range(1,11):
    x = int(input("Digite um numero: "))
    if x >= 10 and x <= 20:
        cont = cont + 1
    else:
        cont2 = cont2 + 1

print("Dentro do intervalo: ", cont)
print("Fora do intervalo: ", cont2)