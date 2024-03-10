def sb(v):
    for i in range(len(v)):
        if v[i] > 0:
            v[i] = 1
        else:
            v[i] = 0

v = []
for i in range(30):
    n = int(input("Digite um número: "))
    v.append(n)

sb(v)

print("Vetor convertido:")
print(v)
