from random import randint

matriz_5x5 = []

for linha in range(5):
    linha = []
    for coluna in range(5):
        linha.append(randint(0, 99))
    matriz_5x5.append(linha)

print("Matriz 5x5:")
for linha_matriz in matriz_5x5:
    print(linha_matriz)

maior_valor = float('-inf')
segundo_maior_valor = float('-inf')

for linha in range(5):
    for coluna in range(5):
        valor = matriz_5x5[linha][coluna]
        if valor > maior_valor:
            segundo_maior_valor = maior_valor
            maior_valor = valor
        elif valor > segundo_maior_valor and valor != maior_valor:
            segundo_maior_valor = valor

print("\nSegundo maior valor na matriz:")
print(segundo_maior_valor)