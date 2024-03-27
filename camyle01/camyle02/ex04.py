def e_triangulo_retangulo(lados):
    lados.sort()
    if lados[0]**2 + lados[1]**2 == lados[2]**2:
        return True
    else:
        return False
def main():
    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o primeiro lado do triângulo: "))
    lado3 = float(input("Digite o primeiro lado do triângulo: "))

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

        if e_triangulo_retangulo([lado1, lado2, lado3]):
            print("Os lados informados formam um triângulo retângulo")
        else:
            print("Os lados informados não formam um triângulo retângulo")
if __name__ == "__main__":
    main()