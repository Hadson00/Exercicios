class Quadrado:
    def __init__(self, lado, area ):
        self.lado = lado
        self.area = area

    def valorLado(self):
        return self.lado
    
if __name__ == "__main__":
    lado = float(input("Informe o lado do quadrado: "))
    area = print(f"Área do quadrado é igual a {lado*lado}")
    quadrado= Quadrado(lado=lado, area=area)
    print("Lado do quadrado: ", quadrado.valorLado())