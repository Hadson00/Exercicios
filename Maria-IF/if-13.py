n = 1
s = 0
m = 0
ix = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        s = s + n
        ix = ix + 1 
    else: 
        m = s / ix
        print("Resultado fina: Soma: ",s ,"Media: ",m)   