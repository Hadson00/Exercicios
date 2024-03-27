import random

m = [0]*10
for x in range(10):
    m[x] = [0]*10
for x in range(10):
    for y in range(10):
        m[x][y] = random.randint(10,50)

cont = 9
soma = 0

for x in range(10):
    soma = soma + m[x][cont]
    cont = cont - 1

for x in range(10):
    print (m[x][:])
print ('Média: ', soma/10)