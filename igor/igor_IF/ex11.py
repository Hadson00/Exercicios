x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

if ((x < y) and (x > z)) or ((x > y) and (x < z)):
    print("A mediana é: ",x)
elif ((y < x) and (y > z)) or ((y > x) and (y < z)):
    print("A mediana é: ",y)
elif ((z < y) and (z > x) or (z > y) and (z < x)):
    print("A mediana é: ",z)