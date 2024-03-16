def substituir_valores(vetor):
    i = 0
    while i < len(vetor):
        if vetor[i] > 0:
            vetor[i] = 1
        else:
            vetor[i] = 0
        i += 1

vetor = []
while len(vetor) < 30:
    numero = float(input("Digite um número: "))
    vetor.append(numero)

substituir_valores(vetor)
print("Vetor com valores substituídos: ", vetor)