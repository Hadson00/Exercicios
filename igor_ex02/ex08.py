import random
tam = 5

mat = [0]*tam
for i in range(tam):
    mat[i] = [0]*tam
print mat

for i in range(tam):
    for j in range(tam):
        mat[i][j] = random.randint(0, 99)
print mat

maior = mat[0][0]
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > maior:
            maior = mat[i][j]
print(maior)

maior2 = 0
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > maior2 and mat[i][j] != maior:
            maior2 = mat[i][j]
print(maior2)