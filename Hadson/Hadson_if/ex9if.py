a = str(input("Digite o nome do primeiro time: "))
x = int(input("Digite o número de gols: "))
b = str(input("Digite o nome do segundo time: "))
y = int(input("Digite o número de gols: "))

if x > y:
    print("Vitória do", a)
elif x == y:
    print("Empate")
else:
    print("Vitória do", b)