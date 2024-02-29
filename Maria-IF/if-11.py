a = int(input("digite um número:"))
b = int(input("digite um número:"))
c = int(input("digite um número:"))

if a > b and a < c or a > c and a < b :
    print("A mediana é:",a)
elif b > a and b < c or b > c and b < a:
    print("A mediana é:",b)
else:
    print("A mediana é:",c)