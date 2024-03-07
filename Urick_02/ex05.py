matriz = []
for i in range(1, 7):
    linha = []
    for x in range(1, 7):
        num = int(input(f"Digite um valor [{i+1}][{x+1}]: "))
        linha.append(num)
        matriz.append(linha)
diagonal_prin = [matriz[i-1][i-1]]
diagonal_prin = [matriz[i][i] for i in range(1, 7)]

print("Matriz: ")
for linha in matriz: 
    print(linha)

print("Diagonal Principal:", diagonal_prin)