n=int(1)
soma=int(0)
decs=int(0)
while n != 0:
    n=int(input("Digite o valor do produto: "))
    if n==0:
        print("Acabou")
    elif n < 0:
        n=int(input("Digite o valor do produto novamente: "))
    else:
        soma+=n
        desc = soma*0,1
    if soma > 1000:
       print("Total a pagar: ",desc)
print("Total a pagar: ",soma)            