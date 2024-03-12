matriz = []
for x in range(1, 7):
    linha = []
    for x in range(1, 7):
        num = int(input(f"Digite um valor [{x+1}][{x+1}]: "))
        linha.append(num)
        matriz.append(linha)
diagonal_prin = [matriz[x-1][x-1]]
diagonal_prin = [matriz[x][x] for x in range(1, 7)]

print("Matriz: ")
for linha in matriz: 
    print(linha)

print("Diagonal Principal:", diagonal_prin)