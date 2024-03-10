def calcular(n):
    result = 0
    m = 3
    
    for i in range(n):
        result += (i+2)/m
        m = m+2

    return result

def principal():
    n=-1
    while n<=0:
        
        n= int(input("Digite um número positivo: "))
        if n <=0:
            print("O número digitado não era positivo")
            n=int(input("Digite novamente: "))
    
    result = calcular(n)
    print(f"O valor da expressão n = {n} é: {result}")

if __name__=="__principal__":
    principal()