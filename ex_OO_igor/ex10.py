class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def tipo_combustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def valor_litro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def quantidade_combustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecer_por_valor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.quantidade_combustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecer_por_litro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.quantidade_combustivel(
                self.quantidadeCombustivel - totalLitros)

bomba = BombaCombustivel('Gasolina', 7.50, 1000)
bomba.abastecer_por_litro(100)
print(f"A quantidade na bomba é: {bomba.quantidadeCombustivel:f} litros")
bomba.abastecer_por_valor(100)
print(f"A quantidade na bomba é: {bomba.quantidadeCombustivel:f} litros")