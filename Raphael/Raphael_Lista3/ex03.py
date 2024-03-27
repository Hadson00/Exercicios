def cont(a,b):
    ix = 0
    for i in range(len (a)):
        if a[i] == b:
            ix = ix + 1
    return(ix)

palavra = str(input("Escreva algo:")) 
letra = str(input("Digite uma letra:")) 

print(cont(palavra,letra))

