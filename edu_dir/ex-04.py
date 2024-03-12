triangulo = []
for i in range(3):
    lado = float(input(f"Digite o valor do {i+1}º lado do triangulo: "))
    triangulo.append(lado)

triangulo.sort()

if triangulo[0] + triangulo[1] + triangulo[2]:
    if triangulo[0]**2 + triangulo[1]**2 == triangulo[2]**2:
        print("Triangulo retangulo")
    else:
        print("Não é um triangulo retangulo") 
else:
    print("Não forma um triangulo")