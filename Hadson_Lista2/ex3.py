def func(vet):
    for i in range(len(vet)):
        if vet[i] < 0:
            vet[i] = 0
        elif vet[i] < 10:
            vet[i] = 1
        else:
            vet[i] = 2
    return vet

vet = []
for i in range(20):
    n = int(input('Digite um valor: '))
    vet.append(n)

func(vet)
print(vet)