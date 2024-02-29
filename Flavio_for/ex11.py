dint = 0
fint = 0
for x in range(1,11):
    n = int(input("Digite um número: "))
    if n >= 10 and n <= 20:
        dint = dint + 1
    else:
        fint = fint + 1

print("total de números dentro do intervalo: ", dint)
print("total de números fora do intervalo: ", fint)