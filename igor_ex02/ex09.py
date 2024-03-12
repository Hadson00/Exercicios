import math

x = input('Digite um valor: ')
if x >= 1 and x <= 3:
    print("O valor será: ", x**2)
elif x == 4 or x == 9:
    print("O valor será: ", math.sqrt(x))
elif x == 6 or x == 7 or x == 8:
    print("O valor será: ", x/9.0)