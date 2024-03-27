class Quadrado():
    def __init__(self, Tam_lado:float):
        self.Tam_lado = Tam_lado
    
    def Mudar_Valor_Lado(self,novo_VLado):
        self.Tam_lado = novo_VLado 

    def Retornar_Valor(self):
        print("O valor dos lados são: ", self.Tam_lado)
    
    def Calcular_Area(self):
        area = self.Tam_lado ** 2
        print(area)

quadrado = Quadrado(50)
novo_VLado = float(input("Digite uma tamanho pro valor do lado: "))
quadrado.Mudar_Valor_Lado(novo_VLado)
quadrado.Retornar_Valor()
quadrado.Calcular_Area()