class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  
        self.combustivel = 0  

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if self.combustivel >= combustivel_necessario:
            self.combustivel -= combustivel_necessario
            print(f"O carro andou {distancia} quilômetros.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade
        print(f"Foram adicionados {quantidade} litros de combustível.")



if __name__ == "__main__":
    consumo = float(input("Informe o consumo do carro (km por litro): "))
    meuFusca = Carro(consumo)

    quantidade_combustivel = float(input("Informe a quantidade de combustível para abastecer (litros): "))
    meuFusca.adicionarGasolina(quantidade_combustivel)

    distancia = float(input("Informe a distância a percorrer (quilômetros): "))
    meuFusca.andar(distancia)

    print(f"Combustível restante no tanque: {meuFusca.obterGasolina()} litros.")
