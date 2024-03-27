import math

def func(v):
    if v[0] > v[1] and v[0] > v[2]:
        h = v[0]
        cat1 = v[1]
        cat2 = v[2]
    elif v[1] > v[0] and v[1] > v[2]:
        h = v[1]
        cat1 = v[0]
        cat2 = v[2]
    else:
        h = v[2]
        cat1 = v[0]
        cat2 = v[1]

    if h == (math.sqrt((cat1 ** 2) + (cat2 ** 2))):
        return 1
    else:
        return 0

v = []
for i in range(3):
    v[i] = int(input('Digite um valor: '))

if func(v) == 1:
    print ('É um triângulo retângulo')
else:
    print ('Não é um triângulo retângulo')