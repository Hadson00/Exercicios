class Calculadora:
    def __innit__(self):
        pass
    def somar(self, valor, valor2):
        return valor + valor2
    def subtrair(self, valor, valor2):
        return valor - valor2
    def multiplicar(self, valor, valor2):
        return valor * valor2
    def dividir(self, valor, valor2):
        if valor2 != 0:
            return valor / valor2
        else:
            return "Erro: Divisão por zero!"

calc = Calculadora()
print("Soma:", calc.somar(5, 3))
print("Subtração:", calc.subtrair(7, 2))
print("Multiplicação:", calc.multiplicar(4, 6))
print("Divisão:", calc.dividir(10, 2))
print("Divisão por zero:", calc.dividir(8, 0))