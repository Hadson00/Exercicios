def valores(vet, tam):
    for x in range(tam):
        if vet[x] < 0:
            vet[x] = 0
        elif vet[x] < 10:
            vet[x] = 1
        else:
            v[x] = 2
    return vet

tam = 39
v = [0] * tam
for x in range(tam):
    v[x] = int(input("Digite um numero: "))
valores(v,tam)
print(v)