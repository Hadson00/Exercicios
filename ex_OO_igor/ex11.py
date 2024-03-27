class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

    def abastecer(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def receber_gasolina(self):
        print(f"{self.qtdeCombustivel:f}")


meuFusca = Carro(15)
meuFusca.abastecer(20)
meuFusca.andar(100)
meuFusca.receber_gasolina()