class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

    def __str__(self):
        return f"Retângulo com vértice inicial {self.ponto_inicial}, largura {self.largura} e altura {self.altura}"


def imprimir_ponto(ponto):
    print(f"Ponto: {ponto}")


def alterar_retangulo(retangulo):
    novo_x = float(input("Novo valor de x para o vértice inicial: "))
    novo_y = float(input("Novo valor de y para o vértice inicial: "))
    nova_largura = float(input("Nova largura: "))
    nova_altura = float(input("Nova altura: "))

    retangulo.ponto_inicial.x = novo_x
    retangulo.ponto_inicial.y = novo_y
    retangulo.largura = nova_largura
    retangulo.altura = nova_altura


if __name__ == "__main__":
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 5, 3)

    while True:
        print("\nMenu:")
        print("1. Imprimir centro do retângulo")
        print("2. Alterar valores do retângulo")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            centro = retangulo.centro()
            print(f"Centro do retângulo: {centro}")
        elif opcao == "2":
            alterar_retangulo(retangulo)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
