import math 
class calculator :
    def soma (self, x, y):
        return x + y

    def subtracao (self, x, y):
        return x - y

    def multiplicacao (self, x, y):
        return x * y
    
    def divisao (self, x, y):
        if x == 0 or y == 0:
            return "ERRO!! Divisão por zero!"
        return x / y
        
    def percentual (self, valor , percentual ):
        return (valor * percentual ) / 100
    def raiz (self, x   ) :
        return math.sqrt (x)
    def potencia (self, b, e ) :
        return b ** e 

def main():
    calculadora = calculator ()

    operacoes = {
        '1': calculadora.soma,
        '2': calculadora.subtracao,
        '3': calculadora.multiplicacao,
        '4': calculadora.divisao,
        '5': calculadora.percentual,
        '6': calculadora.raiz,
        '7': calculadora.potencia,
    }

    operacao = ''
    while operacao != '5':
        print("Escolha a operação que deseja usar ou digite 0 para finalizar:")
        print("1- Somar")
        print("2- Subtrair")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Percentual")
        print("6- Raiz quadrada")
        print("7- Potência")
        
        operacao = input("Digite o número da operação desejada: ")

        if operacao == "0":
            print("Fim do programa")
            break

        elif operacao == '1':
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = calculadora.soma(x, y)
            print(resultado)
    
        elif operacao == '2':
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = calculadora.subtracao(x, y)
            print(resultado)
            
        elif operacao == '3':
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = calculadora.multiplicacao(x, y)
            print(resultado)

        elif operacao == '4':
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = calculadora.divisao(x, y)
            print(resultado)

        elif operacao == '5':
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = calculadora.percentual(x, y)
            print(resultado)

        elif operacao == '6':
            x = float(input("Digite o primeiro número: "))
            resultado = calculadora.raiz(x)
            print(resultado)

        elif operacao == '7':
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = calculadora.potencia(x, y)
            print(resultado)

        else:
            print("Operação inválida!")
        break

if __name__ == "__main__":
    main()

