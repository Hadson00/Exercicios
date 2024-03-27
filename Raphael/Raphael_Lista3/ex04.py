def imc(a,b):
    IMC = a / (b**2)
    return(IMC)

n1 = int(input("Digite seu peso(Kg):"))
n2 = float(input("Digite sua altura(M)"))    

print(imc(n1,n2))