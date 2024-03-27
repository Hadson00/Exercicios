class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, porcentual_de_aumento):
        aumento = self.salario * (porcentual_de_aumento / 100)
        self.salario += aumento


if __name__ == "__main__":
    
    funcionario1 = Funcionario("João", 2000.0)

    print("Nome:", funcionario1.getNome())
    print("Salário:", funcionario1.getSalario())

    
    funcionario1.aumentarSalario(10)  
    print("Salário após aumento:", funcionario1.getSalario())
