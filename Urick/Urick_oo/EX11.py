class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

    def adicionarGasolina(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def obterGasolina(self):
        print(f'{self.qtdeCombustivel:.2f}')

meufusca = Carro(15)
meufusca.adicionarGasolina(20)
meufusca.andar(100)
meufusca.obterGasolina()