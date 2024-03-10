def lt(lados):
    lados.sort()
    
    a2 = lados[0] ** 2
    b2 = lados[1] ** 2
    c2 = lados[2] ** 2
    
    if a2 + b2 == c2:
        return True
    else:
        return False

lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

lados = [lado1, lado2, lado3]

if lt(lados):
    print("Os lados informados formam um triângulo retângulo.")
else:
    print("Os lados informados não formam um triângulo retângulo.")

