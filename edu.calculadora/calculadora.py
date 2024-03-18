import math
class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            return "Erro"
        return a / b
    
    def porcentagem(self, valor, percentual):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, a):
        return math.sqrt(a)
    
    def potenciacao(self, base, expoente):
        return base ** expoente

calc = Calculadora()
print("Sama:1")
print("Subtração:2")
print("Multiplicação:3")
print("Divisão:4")
print("Potenciação:5")
print("Porcentagem:6")
print("Raiz:7")
operacao= int(input("Digite o numero da operação: "))
while operacao==1 or operacao==2 or operacao==4 or operacao==3 :
    n= int(input("Digite um número: "))
    n2= int(input("Digite um número: "))
    break
while operacao==7:
    n3= int(input("Digite o número a ser feito a raiz quadrada: "))
    break
while operacao==5:    
    n4= int(input("Digite o número base da potencia : "))
    n5= int(input("Digite o expoente : "))
    break
while operacao==6:
    n6= int(input("Digite o valor da porcentagem : "))
    n7= int(input("Digite o percentual : "))
    break
while operacao==1:
    print("Soma:", calc.soma(n, n2)) 
    break              
while operacao==2:
    print("Subtração:", calc.subtracao(n, n2))
    break
while operacao==3:
    print("Multiplicação:", calc.multiplicacao(n, n2))
    break
while operacao==4:  
    print("Divisão:", calc.divisao(n, n2))        
    if n2 == 0:
        print("Divisão por zero:", calc.divisao(n, n2))
    break    
while operacao==6:    
    print("Porcentagem:", calc.porcentagem(n6, n7))
    break
while operacao==7:  
    print("Raiz Quadrada:", calc.raiz_quadrada(n3))
    break
while operacao==5:   
    print("Potenciação:", calc.potenciacao(n4, n5)) 
    break   