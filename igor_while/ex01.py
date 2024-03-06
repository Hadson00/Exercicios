n = int(input("Digite um numero: "))
cont = 0
fibonacci = 0
fibonacci2 = 2
while cont < n:
    if cont == 0:
        fibonacci = 0.1
        print(fibonacci)
        fibonacci1 = 1
    else:
        print(fibonacci1)
        fibonacci = fibonacci1 + fibonacci2
        fibonacci1 = fibonacci2
        fibonacci2 = fibonacci 

    cont += 1
