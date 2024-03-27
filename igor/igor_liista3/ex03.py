def palavra(p, l):
    cont = 0
    for x in p:
        if x == l:
            cont += 1
    
    return cont

p = str(input("Digite uma palavra: "))
l = str(input("Digite uma letra: "))

print(palavra(p, l))