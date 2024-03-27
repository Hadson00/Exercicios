class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self): 
        if self.largura %2 == 1 and self.altura %2 == 1:
            largura_centro = (self.largura /2) + 0.5
            altura_centro = (self.altura /2) + 0.5
            print(f"Posição do centro do retangulo: Largura: {largura_centro:f} Altura: {altura_centro:f}")
        else:
            print(f"Valores não encotrados")
    
class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir_ponto(self):
        if self.x == 0 or self.y == 0:
            p = Ponto.iniciar_partida(self)
            print(f"Posição inicial do ponto :Largura: {p[0]} Altura: {p[1]}")
        else:
            print(f"Posição do ponto : Largura: {self.x} Altura: {self.y}")
  
    def iniciar_partida(self):
        larguraInicial = 2
        alturaInicial = self.y - 1
        print(f"Posição inicial do ponto :Largura: {larguraInicial} Altura: {alturaInicial}")
        inicio_ponto = [larguraInicial, alturaInicial]
        return inicio_ponto  


quad1 = Retangulo(7,5)
quad1.encontrar_centro()

quad1 = Ponto(5,6)
quad1.imprimir_ponto()
quad1.iniciar_partida()