class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def retonar_nome(self):
        return self.nome

    def retornar_salario(self):
        return self.salario

    def aumentar_salario(self, percentual_de_aumento):
        self.salario += self.salario * (percentual_de_aumento / 100.00)
        
funcionario = Funcionario("Harry", 25000)
funcionario.aumentar_salario(10)
print ("Nome: ", funcionario.retonar_nome())
print ("Salario: ", funcionario.retornar_salario())