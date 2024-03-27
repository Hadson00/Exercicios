import random

m = [0]*10
for x in range(10):
    m[x] = [0]*10
for x in range(10):
    for y in range(10):
        m[x][y] = random.randint(10,50)
for x in range(10):
    print (m[x][:])

maior = m[1][0]
for x in range(10):
    for y in range(10):
        if x != y:
            if m[x][y] > maior:
                maior = m[x][y]
print ("Maior valor da matriz: ",maior)