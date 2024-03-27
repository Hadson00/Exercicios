di = 0
fi = 0

for ix in range(1,11,1):
    n = int(input("Digite um número: "))
    if ((n > 10) and (n < 20)):
        di = di + 1
    else:
        fi = fi + 1

print("Numeros dentro do intervalo:",di)
print("Numeros fora do intervalo:",fi)