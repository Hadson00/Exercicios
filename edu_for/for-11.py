b=int(1)
c=int(1)
for i in range(1,11):
    a = int(input("Digite um número: "))
    if a > 10 and a < 20:
        b+=b
    elif a < 10 and a > 20:
        c+=c
print("Números no intervalo de 10 e 20: ",b)
print("Números fora do intervalo de 10 e 20: ",c)
