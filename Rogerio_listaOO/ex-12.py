class Investimento:
    nome = None
    numero = None
    saldo = None
    taxJur = None

    def __init__(self, nome, num, sdo, tax):
        self.nome = nome
        self.numero = num
        self.saldo = sdo
        self.taxJur = tax

    def addJur(self):
        self.saldo += (self.taxJur/100)*self.saldo
        return 'O novo valor é {self.saldo}'
nome = input('Nome: ').upper()
num = input('Conta: ')
saldo = float(input('Digite seu valor em R$: '))
tax = float(input('Digite a taxa de Juros: '))

investimento = Investimento(nome, num, saldo, tax)
print(investimento.addJur())
print(investimento.addJur())
print(investimento.addJur())
print(investimento.addJur())
print(investimento.addJur())