class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
    
        if b == 0:
            return
        else:
            return a / b

calc = Calculadora()

num1 = 10
num2 = 5

print("Soma:", calc.soma(num1, num2))
print("Subtração:", calc.subtracao(num1, num2))
print("Multiplicação:", calc.multiplicacao(num1, num2))
print("Divisão:", calc.divisao(num1, num2))