class Conta:

    def __init__(self, numero_conta, nome_conta, saldo_conta):
        self.numero_conta = numero_conta
        self.nome_conta = nome_conta
        self.saldo_conta = saldo_conta

    def alterar_nome(self):
        self.nome_conta = str(input("Trocar o nome da conta: "))
    
    def retornar_nome(self):
        return self.nome_conta
    
    def depositar(self):
        deposito = float(input("Digite o valor do depósito: "))
        self.saldo_conta += deposito 

    def sacar(self):
        saque = float(input("Digite o valor do saque: "))
        self.saldo_conta -= saque

    def retornar_saldo(self):
        return self.saldo_conta

numero_conta = int(input("Digite o numero da sua conta: "))
nome_conta = str(input("Digite o nome da conta: "))
saldo_conta = float(input("Digite o saldo da sua conta: "))

conta = Conta(numero_conta, nome_conta, saldo_conta)
print("Nome da conta: ", conta.retornar_nome())
print("A saldo da conta: R$ ", conta.retornar_saldo())
conta.alterar_nome()
print("Nome da conta: ", conta.retornar_nome())
conta.depositar()
print("Novo saldo da conta: R$ ", conta.retornar_saldo())
conta.sacar()
print("Novo saldo da conta: R$ ", conta.retornar_saldo())