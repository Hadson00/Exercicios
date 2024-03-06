num = int(input("Digite número: "))
quant = 0
fibonacci = 0
fibonacci2 = 2
while quant < num:
    if quant == 0:
        fibonacci = 0.1
        print(fibonacci)
        fibonacci3 = 1
    else:
        print(fibonacci3)
        fibonacci = fibonacci3 + fibonacci2
        fibonacci3 = fibonacci2
        fibonacci2 = fibonacci
    
    quant += 1 
