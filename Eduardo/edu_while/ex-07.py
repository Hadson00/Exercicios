lista = []
while True:
    n = int(input("Digite o número: "))
    if n == 0:
        break
    lista.append(n)

print ("O maior número: ",max(lista)) 