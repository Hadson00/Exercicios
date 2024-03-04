Num1 = int(input("Digite um numero: "))
Num2 = int(input("Digite o ultimo numero: "))
Num2 = Num2 + 1
par = 0
impar = 0 

for y in range(Num1, x):
    if (y % 2) == 0:
        par = par + 1
    else:
        impar = impar + 1

print("Numeros pares: ", par)
print("Numeros Impares: ", impar)