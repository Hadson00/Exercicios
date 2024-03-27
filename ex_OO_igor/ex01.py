class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocarCor(self):
        self.cor = str(input("Digite uma nova cor: "))

    def mostrarCor(self):
        return self.cor
    
b = Bola("preto", 20, "couro")
print("Cor da bola: ", b.mostrarCor())
b.trocarCor()
print("Cor da bola trocada para: ", b.mostrarCor())