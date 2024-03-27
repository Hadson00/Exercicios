class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def receber_nome(self):
        return self.nome

    def receber_salario(self):
        return self.salario


funcionario = Funcionario("Igor Alves", 1200.00)
print (f'Nome: {funcionario.receber_nome()}')
print (f'Salário: R$ {funcionario.receber_salario():f}')