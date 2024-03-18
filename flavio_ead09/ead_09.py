import math
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
    def porcentagem(self, valor, porcentual):
        return valor * (porcentual / 100)
    def raiz_quadrada(self, valor):
        return math.sqrt(valor)
    def potenciacao(self, base, expoente):
        return base ** expoente



calc = Calculadora()
print("Soma:", calc.somar(5, 3))
print("Subtração:", calc.subtrair(7, 2))
print("Multiplicação:", calc.multiplicar(4, 6))
print("Divisão:", calc.dividir(10, 2))
print("Divisão por zero:", calc.dividir(8, 0))
print("Porcentagem:", calc.porcentagem(100, 20))
print("Raiz Quadrada:", calc.raiz_quadrada(25))
print("Potenciação:", calc.potenciacao(2, 3)) 