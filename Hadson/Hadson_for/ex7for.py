i = 0
p = 0

for x in range(1, 101):
    if x % 2 == 0:
        p = p + 1
    else:
        i = i + 1
print("Numeros pares: ",p)     
print("Numeros impares: ",i)