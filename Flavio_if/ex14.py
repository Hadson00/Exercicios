cap = 0
altono = 0
alt = float(input("Digite a altura do reservatorio de água(cm): "))
larg = float(input("Digite a largura do reservatorio de água(cm): "))
comp = float(input("Digite o comprimento do reservatorio de água(cm): "))
cons = float(input("Digite o consumo médio diário dos utilizadores do reservatório(Litros): "))

cap = (alt * larg * comp) / 1000
altono = cap // cons

print("Capacidade total: ", cap)
print("Autonomia do reservatorio: ", altono)

if altono < 2:
    print("Consumo elevado")
elif altono <= 7:
    print("Consumo moderado")
else:
    print("Consumo reduzido")