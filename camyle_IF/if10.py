#12-  Escreva um programa em Python para calcular o fatorial de qualquer número inteiro.

n = int(input("Digite um numero inteiro:"))
if n < 0 :
    print("o fatorial negativo não é definido")
elif n == 0 :
    print ("O fatorial de 0 é 1 ")
else :
    fatorial = 1
    for i in range(1, n + 1) :
        fatorial *= i
        print("O fatorial de", n, "é", fatorial)

 
    