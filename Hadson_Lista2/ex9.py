import math

n = float(input('Digite um valor: '))
if n >= 1 and n <= 3:
    print (n**2)
elif n == 4 or n == 9:
    print (math.sqrt(n))
elif n >= 6 and n <= 8:
    print (n/9)