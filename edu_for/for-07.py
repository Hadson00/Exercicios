p = int(0)
imp = int(0)
a = int(input("Digite um número: "))
for i in range(1,a+1):
    if i % 2 == 0:
        p = p + 1
    else:
        imp = imp + 1

print("Quantidade de números impares: ",imp)
print("Quantidade de números pares: ",p)
