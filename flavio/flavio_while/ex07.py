num = True
m = 0
while num:
    x = int(input("Digite um número: "))
    if x > m:
        m = x
    else: 
        num = False

print("O maior número digitado é: ", m)