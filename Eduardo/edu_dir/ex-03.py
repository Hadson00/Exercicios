vet = []

for i in range(20):
    n = float(input(f"Digite o {i+1}ª número: "))
    vet.append(n)

for i in range(len(vet)):
    if vet[i]<0:
        vet[i]=0
    elif vet[i]<10:
        vet[i]=1
    else:
        vet[1]=2

print("Valores substituídos: ")
print(vet)  