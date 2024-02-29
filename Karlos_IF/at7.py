i=float(input("Digite um numero positivo: "))
a=float(input("Digite um numero: "))
b=float(input("Digite um numero: "))
c=float(input("Digite um numero: "))

if (i % 2 == 0) and (i < 10):
    print("média aritmética: ", (a+b+c)/3)
elif (i % 2 == 1) and (i < 10):
    print("media ponderada: ", ((a*2)+(b*3)+(c*4))/9)
elif i > 10: 
    print("média aritmética: ", (a+b+c)/3)
    print("media ponderada: ", ((a*2)+(b*3)+(c*4))/9)