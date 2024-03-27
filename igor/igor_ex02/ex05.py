vetor = [0]*6
matriz = [0]*6
for x in range(6):
    matriz[x] = [0]*6

for lin in range(6):
    for col in range(6):
        mat[lin][col] = input("Digite um valor: ")
print(matriz)

for lin in range(6):
    for col in range(6):
        print lin,col
        if lin == col:
            print('DP', lin, col)
            vetor[lin] = matriz[lin][col]
print(vetor)