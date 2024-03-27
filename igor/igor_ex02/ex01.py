def valores(valor):
    cont = 0
    while cont < len(vetor):
        if vetor[cont] > 0:
            vetor[cont] = 1
        else:
            vetor[cont] = 0
        cont = cont + 1

vetor = []
while len(vetor) < 30:
    n = float(input("Digite um valor: "))
    vetor.append(n)

valores(vetor)
print("valores trocados: ", vetor)