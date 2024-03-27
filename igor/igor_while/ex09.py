x = 1
s = 0
cont = 0
m = 0.0
while x != 0:
    x = int(input("Digite um numero: "))
    if x != 0:
        s = s + x
        cont = cont + 1

if cont == 0:
    print("Numero errado")
else:
    m = s / cont

print("A soma será: ", s)
print("A media será: ", m)