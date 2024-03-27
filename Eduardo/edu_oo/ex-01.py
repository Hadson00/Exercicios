class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

if __name__ == "__main__":
    cor = input("Insira a cor da bola: ")
    circunferencia = float(input("Insira a circunferência da bola: "))
    material = input("Insira o material da bola: ")
    bola = Bola(cor=cor, circunferencia=circunferencia, material=material)
    print("Cor inicial da bola:", bola.mostraCor())
    nova_cor = input("Insira a nova cor da bola: ")
    bola.trocaCor(nova_cor)
    print("Nova cor da bola:", bola.mostraCor())