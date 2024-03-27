vet = []

for i in range(30):
    n = float(input(f"Digite o {i+1}ª número: "))
    vet.append(n)

for i in range(len(vet)):
    if vet[i] > 0:
        vet[1] = 1
    else:
        vet[i] = 0

print("Valores substituídos: ")
print(vet)    