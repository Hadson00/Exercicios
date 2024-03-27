n = int(input("Digite um número positivo (digite 0 para parar): "))
mn = n
while n != 0:
    if n > 0:
        if n > mn:
            mn = n
        n = int(input("Digite um número positivo (digite 0 para parar): "))   
    else: 
        print("Número negativo, por favor digite um número positivo")        
        n = int(input("Digite um número positivo (digite 0 para parar): "))   

print("O maior número é:",mn)    