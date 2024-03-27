from random import randint

matriz_10x10 = []

for linha in range(10):
    linha = []
    for coluna in range(10):
        linha.append(randint(10, 50))
    matriz_10x10.append(linha)

for linha_matriz in matriz_10x10:
    print(linha_matriz)

maior_valor = None

print("\nMaior valor na matriz desconsiderando a diagonal principal:")
for linha in range(10):
    for coluna in range(10):
        if linha != coluna:  # Ignora os elementos da diagonal principal
            if maior_valor is None or matriz_10x10[linha][coluna] > maior_valor:
                maior_valor = matriz_10x10[linha][coluna]

print(maior_valor)