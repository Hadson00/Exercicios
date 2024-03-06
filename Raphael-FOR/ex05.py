n = int(input("Digite um número:"))

for ix in range(n,1,-1):
    n = n + (ix - 1)


print("Soma final:", n)