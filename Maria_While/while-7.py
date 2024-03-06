n = int(input("Digite um número:"))
nm = n 
while n != 0:
    if n > nm:
        nm = n
    n = int(input("Digite um número positivo (Caso queira parar,digite 0): ")) 
    print("O maior número digitado acima é:",nm)  