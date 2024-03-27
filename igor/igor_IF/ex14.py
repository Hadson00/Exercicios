t = 0
r = 0

a = float(input("Digite a altura em centimetros: "))
l = float(input("Digite a largura em centimetros: "))
c = float(input("Digite o comprimento em centimetros: "))
d = float(input("Digite o consumo do reservatório em litros: "))

t = (a * l * c) / 1000
r = t // d 

print("Capacidade total: ", t)
print("Autonomia do reservatório: ", r)
if r < 2:
    print("Consumo elevado")
elif (r >= 2) and (r <= 7):
    print("Consumo moderado")
else:
    print("Consumo reduzido")
