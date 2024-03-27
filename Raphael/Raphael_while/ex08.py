n = float(input("Digite o valor do produto: "))
s = 0
st = 0
while n != 0:
    if n > 0:
        s = s + n
        n = float(input("Digite o valor do produto: "))   
    else: 
        print("Número negativo, por favor digite um valor positivo")        
        n = float(input("Digite o valor do produto: "))   

if s >= 1000:
    st = s - (s * 0.1)
    print("O Valor da compra é de:",st)      
else:
    st = s 
    print("O Valor da compra é de:",st) 