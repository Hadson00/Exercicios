def func(vetor):
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = 1
        else:
            vetor[i] = 0
    return vetor

vetor = []
for i in range(30):
    n = int(input('Digite um valor: '))
    vetor.append(n)

func(vetor)
print (vetor)