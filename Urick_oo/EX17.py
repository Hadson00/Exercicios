import random

class Bichinho:
    def __init__(self, nome):
        self._nome = nome
        self._fome = random.randint(0, 10)
        self._tedio = random.randint(0, 10)

    @property
    def nome(self):
        return self._nome

    @property
    def fome(self):
        return self._fome

    @property
    def tedio(self):
        return self._tedio

    def alimentar(self):
        self._fome -= 1
        if self._fome < 0:
            self._fome = 0

    def brincar(self):
        self._tedio -= 1
        if self._tedio < 0:
            self._tedio = 0

    def ouvir(self):
        print(f"{self._nome} diz: 'Oiiii!'")

class FazendaBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_todos(self):
        for bichinho in self.bichinhos:
            bichinho.alimentar()

    def brincar_todos(self):
        for bichinho in self.bichinhos:
            bichinho.brincar()

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            bichinho.ouvir()

# Exemplo de uso
fazenda = FazendaBichinhos()
fazenda.adicionar_bichinho(Bichinho("João"))
fazenda.adicionar_bichinho(Bichinho("Maria"))

opcao = ""
while opcao != "sair":
    print("\nMenu:")
    print("1 - Alimentar todos os bichinhos")
    print("2 - Brincar com todos os bichinhos")
    print("3 - Ouvir todos os bichinhos")
    print("sair - Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazenda.alimentar_todos()
    elif opcao == "2":
        fazenda.brincar_todos()
    elif opcao == "3":
        fazenda.ouvir_todos()
    elif opcao == "sair":
        print("Saindo do programa...")
    else:
        print("Opção inválida!")
