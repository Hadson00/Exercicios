x = True
m = 0

while x:
    num = int(input("Digite um numero positivo: "))
    if num > m:
        m = num
    elif num == 0:
        x = False

print("O numero maior é: ", m)
        

