x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
z = int(input("Digite outro número: "))

if ((x < y) and (x > z)) or ((x > y) and (x < z)):
    print("A mediana é:",x)
elif ((y < x) and (y > z)) or ((y > x) and (y < z)):
    print("A mediana é:",y)
elif ((z < y) and (z > x)) or ((z > y) and (z < x)):
    print("A mediana é:",z)