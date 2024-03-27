class Funcionario:

    nome = None
    salario = None

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def nomeFunc(self):
        return self.nome

    def Salario(self):
        return self.salario

nome = input('Nome: ').upper()
salario = float(input('Salário: '))
Func = Funcionario(nome, salario)
print(f'O nome do(a) funcionário(a) é {Func.nomeFunc()} e o seu salário é de R${Func.Salario()}')