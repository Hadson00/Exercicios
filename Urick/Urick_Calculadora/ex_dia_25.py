class BombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self._tipoCombustivel = tipoCombustivel
        self._valorLitro = valorLitro
        self._quantidadeCombustivel = quantidadeCombustivel

    @property
    def tipoCombustivel(self):
        return self._tipoCombustivel
    
    @property
    def valorLitro(self):
            return self._valorLitro
        
    @property
    def quantidadeCombustivel(self):
        return self._quantidadeCombustivel 
        
    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self._valorLitro
        if litros_abastecidos <= self._quantidadeCombustivel:
            self._quantidadeCombustivel -= litros_abastecidos
            return litros_abastecidos
            
    def abastecerPorLitros(self, litros):
        valor_pagar = litros * self._valorLitro
        return valor_pagar
    
    def alterarValor(self, novo_valor):
         self._valorLitro = novo_valor

    def alterarCombustivel(self, novo_tipo):
         self._tipoCombustivel = novo_tipo

    def alterarQuantidadeCombustivel(self, nova_quantidade):
         self._quantidadeCombustivel = nova_quantidade

bomba = BombaCombustivel("Gasolina",5.50,100.0)
print(f"Tipo de combustível:{bomba.tipoCombustivel}")
print(f"Valor Litro:{bomba.valorLitro}")
print(f"Quantidade de combustível:{bomba.quantidadeCombustivel}litros")

litros_abastecidos = bomba.abastecerPorValor(6)
print(f"{litros_abastecidos:.2f} litros abastecidos")

valor_pagar = bomba.abastecerPorLitros(3)
print(f"Valor a pagar: R${valor_pagar}")

bomba.alterarValor(5.5)
bomba.alterarCombustivel("Álcool")
bomba.alterarQuantidadeCombustivel(150.0)

print(f"Novo valor do litro: {bomba.valorLitro}")
print(f"Novo tipo de combustível: {bomba.tipoCombustivel}")
print(f"Nova quantidade de combustível: {bomba.quantidadeCombustivel:.2f}")