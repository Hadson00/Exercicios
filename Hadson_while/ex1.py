x = int(input("Digite um número: "))
ant = 0
prox = 1
soma = 1

for i in range(0,x):
    print(ant)
    soma = prox + ant
    ant = prox
    prox = soma