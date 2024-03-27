class Quadrado:

    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def mudarvalor(self):
        self.tamanhoLado = int(input("Digite um novo valor: "))

    def retornarvalor(self):
        return self.tamanhoLado
    
    def calcular(self):
        return self.tamanhoLado * self.tamanhoLado

quadrado = Quadrado(2)
print("Lado do quadrado: ", quadrado.retornarvalor())
print("Area do quadrado: ", quadrado.calcular())
quadrado.mudarvalor()
print("Lado do quadrado trocado para: ", quadrado.retornarvalor())
print("Area do quadrado: ", quadrado.calcular())
        