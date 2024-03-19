import math
class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, numero, numero2):
        return numero + numero2
    
    def subtracao(self, numero, numero2):
        return numero - numero2
    
    def multiplicacao(self, numero, numero2):
        return numero * numero2
    
    def divisao(self, numero, numero2):
        if numero2 == 0:
            return "Erro"
        return numero / numero2
    
    def porcentagem(self, valor, percentual):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, numero):
        return math.sqrt(numero)
    
    def potenciacao(self, base, expoente):
        return base ** expoente

calc = Calculadora()
operacao=None
while True:
    print("_________________________________________")
    print("Soma:1")
    print("Subtração:2")
    print("Multiplicação:3")
    print("Divisão:4")
    print("Potenciação:5")
    print("Porcentagem:6")
    print("Raiz:7")
    operacao= int(input("Digite o número da operação: "))
    while operacao==1 or operacao==2 or operacao==4 or operacao==3 :
        numero= int(input("Digite um número: "))
        numero2= int(input("Digite um número: "))
        break
    while operacao==7:
        numero3= int(input("Digite o número a ser feito a raiz quadrada: "))
        break
    while operacao==5:    
        numero4= int(input("Digite o número base da potencia : "))
        numero5= int(input("Digite o expoente : "))
        break
    while operacao==6:
        numero6= int(input("Digite o valor da porcentagem : "))
        numero7= int(input("Digite o percentual : "))
        break
    while operacao==1:
        print("Soma: ", calc.soma(numero, numero2)) 
        break              
    while operacao==2:
        print("Subtração:", calc.subtracao(numero, numero2))
        break
    while operacao==3:
        print("Multiplicação:", calc.multiplicacao(numero, numero2))
        break
    while operacao==4:  
        print("Divisão:", calc.divisao(numero, numero2))        
        if numero2 == 0:
            print("Divisão por zero:", calc.divisao(numero, numero2))
        break    
    while operacao==6:    
        print("Porcentagem:", calc.porcentagem(numero6, numero7))
        break
    while operacao==7:  
        print("Raiz Quadrada:", calc.raiz_quadrada(numero3))
        break
    while operacao==5:   
        print("Potenciação:", calc.potenciacao(numero4, numero5)) 
        break   
    if operacao==0:
        print("Calculadora encerrada")
        break