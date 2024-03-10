import math

def hipo(vetor):
    if vetor[0] > vetor[1] and vetor[0] > vetor[2]:
        hipotenusa = vetor[0]
        cateto1 = vetor[1]
        cateto2 = vetor[2]
    elif vetor[1] > vetor[0] and vetor[1] > vetor[2]:
        hipotenusa = vetor[1]
        cateto1 = vetor[0]
        cateto2 = vetor[2]
    else:
        hipotenusa = vetor[2]
        cateto1 = vetor[0]
        cateto2 = vetor[1]
    print(hiponetusa, cateto1, cateto2)

    if hipotenusa == math.sqrt(cateto1**2 + cateto2**2):
        return 1
    else:
        return 0

vetor = [0]*3
for x in range(3):
    vetor[x] = input("Digite um valor: ")

if hipo(vetor) == 1:
    print("É retangulo")
else:
    print("Não é retangulo")