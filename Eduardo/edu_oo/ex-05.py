class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

numero_conta = input("Digite o número da conta: ")
nome_correntista = input("Digite o nome do correntista: ")
saldo_inicial = float(input("Digite o saldo inicial (opcional, pressione Enter para deixar como zero): ") or 0)
conta = ContaCorrente(numero_conta, nome_correntista, saldo_inicial)
print(f"\nSaldo inicial: R${conta.saldo:.2f}")
while True:
    print("\nEscolha uma operação:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Alterar nome do correntista")
    print("4. Sair")
    opcao = input("Digite o número da operação desejada: ")
    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.deposito(valor_deposito)
    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        conta.saque(valor_saque)
    elif opcao == "3":
        novo_nome = input("Digite o novo nome do correntista: ")
        conta.alterarNome(novo_nome)
        print("Nome do correntista alterado com sucesso.")
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
