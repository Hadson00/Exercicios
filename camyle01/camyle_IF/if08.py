#7- Escrever um programa em linguagem Python que lê um valor i, 
# inteiro e positivo e 3 valores a, b e c. Se o valor de i é par então calcular 
# e imprimir na tela a média aritmética de a, b e c. 
# Caso contrário, se i>10 então calcular e imprimir na tela 
# a média aritmética e ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4.

i = int (input("digite um valor inteiro e positivo para i:"))
if i <= 0 or 1 % 2 != 0 :
    print("o valor 1 é inteiro e positivo par")
else :
    a = float (input("digite o valor de a:"))
    b = float (input("digite o valor de b:"))
    c = float (input("digite o valor de c:"))

    media_ponderada = (a * 2 + b * 3 + c * 4) / (2 + 3 + 4)
    print("A média ponderada é:", media_ponderada)