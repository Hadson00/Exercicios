class Retangulo:
    def __init__(self, ladoA, ladoB, area, perimetro):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.area = area
        self.perimetro = perimetro

    def valorLadoA(self):
         return self.ladoA
    
    def valorLadoB(self):
        return self.ladoB
    
if __name__ == "__main__":
    ladoA = float(input("Informe a base do retangulo: "))
    ladoB = float(input("Informe a altura do retangulo: "))
    area = print(f"Área do retangulo é igual a {ladoA*ladoB}")
    perimetro = print(f"Perimetro do retangulo é igual a {(ladoA*ladoB)*2}")
    retangulo = Retangulo(ladoA=ladoA, ladoB=ladoB, area=area, perimetro=perimetro)
    print("Base do retangulo: ", retangulo.valorLadoA())
    print("Altura do retangulo: ", retangulo.valorLadoB())