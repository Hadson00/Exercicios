x = 1
s = 0
m = 0
cont = 0

while x != 0:
    x = int(input("Digite um numero: "))
    if x != 0:
        s = s + x
    else:
        break
    cont = cont + 1

m = s / cont

print("a soma será: ", s)

print("a media será: ", m)