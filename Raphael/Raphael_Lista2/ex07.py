import random

m = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(random.randint(10, 50))
    m.append(linha)

print("Matriz 10x10:")
for linha in m:
    print(linha)

mv = 0
for i in range(10):
    for j in range(10):
        if i != j:  
            if (mv == 0) or (m[i][j] > mv):
                mv = m[i][j]

print("O maior valor na matriz, desconsiderando a diagonal principal, é:", mv)