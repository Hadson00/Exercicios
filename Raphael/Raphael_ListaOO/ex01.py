class Bola():
    def __init__(self, cor:str, circunferencia:float, material:str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self,nova_cor):
        self.cor = nova_cor
        return self.cor
        
    def mostrarCor(self):
        print("A cor da bola é: ",self.cor)

    def __str__(self):
        return f"A bola é {self.cor} com a circunferencia de {self.circunferencia} feita de {self.material}"

bola = Bola("Azul",50,"Madeira")

print(bola)
nova_cor = str(input("Digite uma nova cor: "))
bola.trocarCor(nova_cor)
bola.mostrarCor()
print(bola)
