i = True
maior = 0

while i:
    num = int(input("Digite um numero: "))
    if num > maior:
        maior = num
    if num == 0:
        i = False
print(maior)