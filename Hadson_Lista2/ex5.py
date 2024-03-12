vetor = [0]*6
matriz = [0]*6
for x in range(6):
    matriz[x] = [0]*6

for lin in range(6):
    for col in range(6):
        matriz[lin][col] = input('Digite um valor: ')

for lin in range(6):
    for col in range(6):
        if lin == col:
            vetor[lin] = matriz[lin][col]
for lin in range(6):
    print (matriz[lin][:])
print (vetor)