num1 = 0
num2 = 0
for x in range(1,11):
    n = int(input("Digite qualquer numero: "))
    if n >= 10 and n <= 20:
        num1 = num1 + 1
    else:
        num2 = num2 + 1

print("numeros dentro do intervalo: ", num1)
print("numeros fora do intervalo: ", num2)