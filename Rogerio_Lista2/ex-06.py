import random

m = [[random.randint(10, 50) for i in range(10)] for j in range(10)]

print("Matriz 10x10:")
for linha in m:
    print(linha)


sds = 0
for i in range(10):
    sds += m[i][9 - i]

mds = sds / 10

print("Média dos elementos da diagonal secundária:", mds)