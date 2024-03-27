import math

class Calculadora:
    def __init__(self, number1:float, number2:float)->None:
        self.number1 = number1
        self.number2 = number2

    def somar(self):
        print("Soma:", self.number1 + self.number2)

    def subtrair(self):
        print("Subtração:", self.number1 - self.number2)

    def multiplicar(self):
        print("Multiplicação:", self.number1 * self.number2)

    def dividir(self):
        if number2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print("Divisão:", self.number1 / self.number2)

    def porcentagem(self):
        print("Porcentagem:", (self.number1 * self.number2) / 100)

    def raiz_quadrada(self):
        print("Raiz quadrada:", math.sqrt(self.number1))

    def potenciacao(self):
        print("Potenciação:", self.number1 ** self.number2)

operacao = 1

while operacao != 0:
    
    operacao=(input("Digite uma operação para fazer +, -, *, /, %, rq(raiz quadrada), p(porcentagem) ou 0 para terminar: "))
    
    if operacao == "+":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.somar()

    elif operacao == "-":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.subtrair()

    elif operacao == "*":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.multiplicar()

    elif operacao == "/":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.dividir()

    elif operacao == "%":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.porcentagem()

    elif operacao == "rq":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.raiz_quadrada()

    elif operacao == "p":
        number1=float(input("Digite um numero:"))
        number2=float(input("Digite outro numero:"))
        calc = Calculadora(number1, number2)
        calc.potenciacao()

    else:
        break