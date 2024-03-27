n=int(1)
soma=int(0)
while True:
    n=int(input("Digite o valor do produto: "))
    if n==0:
        break
    else:
        soma+=n
print("Total a pagar: ",soma)