class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarvalor(self):
        self.base = int(input("Digite uma nova base: "))
        self.altura = int(input("Digite uma nova altura: "))

    def retornarvalor(self):
        print(f"Base : {self.base} e Altura: {self.altura}")
    
    def calcular(self):
        print("A area do retangulo será: ", self.base * self.altura)
        print("O perimetro do retangulo será: ", 2 * (self.base + self.altura))
    
    
retangulo = Retangulo(4, 6)
retangulo.retornarvalor()
retangulo.calcular()
retangulo.mudarvalor()
retangulo.retornarvalor()
retangulo.calcular()

    