def sb(v):
    for i in range(len(v)):
        if v[i] < 0:
            v[i] = 0
        elif v[i] < 10:
            v[i] = 1
        else:
            v[i] = 2

v = []
for _ in range(20):
    n = float(input("Digite um número: "))
    v.append(n)

sb(v)

print("Vetor após a conversão:")
print(v)