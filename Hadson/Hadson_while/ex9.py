i = True
soma = 0
media = 0
cont = 0

while i:
    num = float(input("Digite um número: "))
    soma = soma + num
    cont += 1
    if num == 0:
        cont -= 1
        i = False
media = soma/cont

print(soma)
print(media)