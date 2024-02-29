a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))
n1 = 0
n2 = 0
n3 = 0

if ((a >= b) and (a >= c)):
    n3 = a
    if ((b >= c)):
        n2 = b
        n1 = c
        print("Media mediana é ",n1 ,n2 ,n3)
    else:
        n2 = c
        n1 = b
        print("Media mediana é ",n1 ,n2 ,n3)
elif ((b >= a) and (b >= c)):
    n3 = b
    if ((a >= c)):
        n2 = a
        n1 = c
        print("Media mediana é ",n1 ,n2 ,n3)
    else:
        n2 = c
        n1 = a
        print("Media mediana é ",n1 ,n2 ,n3) 
else: 
    n3 = c
    if ((a >= b)):
        n2 = a
        n1 = b
        print("Media mediana é ",n1 ,n2 ,n3)
    else:
        n2 = b
        n1 = a
        print("Media mediana é ",n1 ,n2 ,n3)  
