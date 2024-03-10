m = [[0 for _ in range(6)] for _ in range(6)]

print("Digite os números para preencher a matriz 6x6:")
for i in range(6):
    for j in range(6):
        m[i][j] = int(input(f"Digite o número para a posição [{i+1}][{j+1}]: "))

print("Matriz 6x6:")
for linha in m:
    print(linha)

diagonal = [m[i][i] for i in range(6)]

print("Elementos da diagonal principal:")
print(diagonal)