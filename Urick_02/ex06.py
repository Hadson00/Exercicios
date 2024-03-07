from random import randint
matriz_10x10 = []

for linha in range(10):
    linha = []
    for coluna in range(10):
        linha.append(randint(10, 50))
    matriz_10x10.append(linha)

for linha_matriz in matriz_10x10:
    print(linha_matriz)

soma_diagonal = 0
media_diagonal = 0
print("Diagonal da matriz:")
for i in range(10):
    print(matriz_10x10[i][i], end=" ")
soma_diagonal += matriz_10x10[0][0] + matriz_10x10[1][1] + matriz_10x10[2][2] + matriz_10x10[3][3] + matriz_10x10[4][4] + matriz_10x10[5][5] + matriz_10x10[6][6] + matriz_10x10[7][7] + matriz_10x10[8][8] + matriz_10x10[9][9] 
media_diagonal = soma_diagonal / 9
print(f"\nSoma da Diagonal: {soma_diagonal}")
print(f"\nSoma da Diagonal: {media_diagonal:.2f}")