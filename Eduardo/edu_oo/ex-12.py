class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  

    def adicioneJuros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

    def getSaldo(self):
        return self.saldo


if __name__ == "__main__":
    saldo_inicial = 1000.00
    taxa_juros = 10.0  

    poupanca = ContaInvestimento(saldo_inicial, taxa_juros)

    for i in range(5):
        poupanca.adicioneJuros()
        print(f"Saldo após {i+1} períodos de juros: R${poupanca.getSaldo():.2f}")
