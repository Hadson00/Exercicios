class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Ponto na posição X: {self.x} e Y: {self.y} \n"

class Retangulo:
    def __init__(self, largura, altura, ponto_inicio):
        self.largura = largura
        self.altura = altura
        self.ponto_inicio = ponto_inicio

    def centro_retangulo(self):
        x = self.ponto_inicio.x + (self.largura / 2)
        y = self.ponto_inicio.y + (self.altura / 2)
        centro = Ponto(x, y)
        print("Centro:", centro)

    def __str__(self):
        return f"Retângulo: largura: {self.largura} altura: {self.altura} \nInicio em x: {self.ponto_inicio.x} e y: {self.ponto_inicio.y} \n"
    
def menu():
    ret = criar_retangulo()
    executar = True

    while executar:
        print(ret)

        print("1 - Criar Retângulo")
        print("2 - Ver centro")
        print("3 - Sair")
        op = input("Selcione uma opção = ")
        print()

        if op == "1":
            ret = criar_retangulo()

        elif op == "2":
            ret.centro_retangulo()
            cont = input("Pressione qualquer tecla para continuar...")
        elif op == "3":
            executar = False

def criar_retangulo():
    print("------ Criar Retangulo ------")

    inicio = Ponto(0, 0)
    ret = Retangulo(5, 5, inicio)
    largura = float(input("Largura: "))
    altura = float(input("Altura: "))

    ret.largura = largura
    ret.altura = altura

    x = float(input("Eixo X: "))
    y = float(input("Eixo Y: "))

    inicio = Ponto(x, y)
    ret.ponto_inicio = inicio

    return ret

menu()