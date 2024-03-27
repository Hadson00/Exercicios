class Conta_Correnete():
    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nomeCorrentista = novo_nome

    def Depositar(self, novo_deposito):
        self.saldo += novo_deposito

    def Sacar(self, saque):    
        self.saldo -= saque

    def __str__(self):
        return f"O número da conta é {self.numeroConta}, o nome do corentista é {self.nomeCorrentista} com o saldo de {self.saldo}."

conta = Conta_Correnete(124094-45,"Raphael",1000)

novo_nome = (str(input("Digite um nome: ")))
conta.alterarNome(novo_nome)
novo_deposito = float(input("Digite o valor do deposito: "))
conta.Depositar(novo_deposito)
saque = float(input("Digite o valor do saque: "))
conta.Sacar(saque)
print(conta)