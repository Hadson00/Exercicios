x = float(input("Valor do Salario: "))

if x < 500:
    x = x - (x * 0.15)
    print(x)
elif (x > 500) and (x < 1000):
    x = x - (x * 0.10)    
    print(x)
else:
    x = x - (x * 0.05)
    print(x)   