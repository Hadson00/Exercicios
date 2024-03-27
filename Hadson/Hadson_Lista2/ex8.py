import random

m = [0]*5
for x in range(5):
    m[x] = [0]*5
for x in range(5):
    for y in range(5):
        m[x][y] = random.randint(5,50)
for x in range(5):
    print (m[x][:])

maior = m[0][0]
for x in range(5):
    for y in range(5):
        if x != y:
            if m[x][y] > maior:
                maior = m[x][y]
smaior = 0
for x in range(5):
    for y in range(5):
        if m[x][y] > smaior and m[x][y] != maior:
            smaior = m[x][y]

print ("Segundo maior valor da matriz: ",smaior)