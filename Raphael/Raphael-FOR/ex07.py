n = int(input("Digite um número: "))
i = 0
p = 0
"""if n > 0:
    while n != 0:
        if (n % 2) == 0:
            p = p + 1
            n = int(input("Digite um número: "))
        elif n == 0: 
            print("Impares",i)
            print("Pares",p)   
        else:
            i = i + 1
            n = int(input("Digite um número: "))
    print("Impares",i)
    print("Pares",p)             
else: print("Fim do Programa")    
"""
for ix in range(1,(n + 1),1):
    if (ix % 2) == 0:
        p = p + 1

    else:
        i = i + 1
    
print("Impares",i)
print("Pares",p)             