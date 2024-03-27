a = float(100)
l = float(100)
c = float(100)
cmd = float(1.3)

t = (a*l*c)/1000
print(t)

aut = t / cmd
aut = aut / 100
print(aut)

if aut < 2:
    print("Consumo elevado")
elif aut >= 2 and aut <= 7:
    print("Consumo moderado")
elif aut > 7:
    print("Consumo reduzido")


