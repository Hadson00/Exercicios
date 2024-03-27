v = 1
vf = 0
x = True
while x:
    v = float(input("Digite um valor inteiro positivo: "))
    if v > 0:
        vf = vf + v
    elif v == 0:
        x = False
    else:
        continue

if vf > 1000:
    vf = vf * 0.9

print("O valor total a pagar será de: ", vf)    