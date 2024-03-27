class Retangulo():

    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura

    def Mudar_Valor_Lado(self, nova_base, nova_altura):
        self.base = nova_base 
        self.altura = nova_altura 
    def Retornar_Valor(self):
        print(f"O valor da base é: {self.base}cm")
        print(f"O valo da altura é: {self.altura}cm")
    
    def Calcular_Area(self):
        area = self.base * self.altura 
        print(f"Area do retangulo {area}cm²")
        return area

    def Calcular_perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        print(f"Perimetro do retangulo {perimetro}")


piso = Retangulo(None,None)
nova_base = float(input("Digite uma tamanho pra base (cm): "))
nova_altura = float(input("Digite uma tamanho pra altura (cm): "))

piso.Mudar_Valor_Lado(nova_base, nova_altura)
piso.Retornar_Valor()
piso.Calcular_Area()
piso.Calcular_perimetro()
x = piso.Calcular_Area()

local = int(input("Area do Local: "))
pisos = local / x
print(f"precisa de {pisos} pisos")