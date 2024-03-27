class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, porcentualDeAumento):
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento
        print(f"O salário de {self.nome} foi aumentado em {porcentualDeAumento}%. Novo salário: R${self.salario:.2f}")


if __name__ == "__main__":
    harry = Funcionario("Harry", 25000)
    harry.aumentarSalario(10)
