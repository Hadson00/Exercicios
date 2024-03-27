import random

m = []
for _ in range(5):
    linha = []
    for _ in range(5):
        linha.append(random.randint(0, 99))
    m.append(linha)

print("Matriz 5x5:")
for linha in m:
    print(linha)

mv = 0
smv = 0

for linha in m:
    for v in linha:  
        if v > mv:
            mv = v
        elif v > smv and v != mv:
            smv = v

print("O segundo maior valor na matriz é:", smv, mv)