x = 1
s = 0
m = 0
ix = 0

while x != 0:
    x = int(input("Digite um número: "))
    if x != 0:
        s = s + x
    else:
        break
    ix = ix + 1

m = s / ix

print(s)

print(m)