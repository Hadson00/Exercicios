class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.nomeCorrentista = nomeCorrentista
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterar_nome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def adicionar_juros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

conta = ContaInvestimento(12345678, "Igor", 10)
conta.depositar(1000)
print(f"R$ {conta.saldo:f}")
conta.adicionar_juros()
print(f"R$ {conta.saldo:f}")
conta.adicionar_juros()
print(f"R$ {conta.saldo:f}")
conta.adicionar_juros()
print(f"R$ {conta.saldo:f}")
conta.adicionar_juros()
print(f"R$ {conta.saldo:f}")