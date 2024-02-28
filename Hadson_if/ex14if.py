t = 0
au = 0

x = float(input("Digite a altura(cm): "))
y = float(input("Digite a largura(cm): "))
z = float(input("Digite e o comprimento(cm): "))
a = float(input("Digite seu consumo diário(Litros): "))

t = (x * y * z) / 1000

au =  t // a

print("Capacidade total do reservatório(Litros): ", t)
print("Autonomia do reservatório(dias): ", au)

if au < 2:
    print("Consumo elevado")
elif au >= 2 and au <= 7:
    print("Consumo moderado")
else:
    print("Consumo reduzido")