import math
n = float(input('Digite um valor: '))
if n == 1 or n == 2:
    print (n**3)
elif (n % 3) == 0:
    print (math.factorial(n))
elif n == 4 or n == 5 or n == 7 or n == 8:
    print (n/9)
else:
    print ('Valor inválido')