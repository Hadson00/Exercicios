import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)  
        self.tedio = random.randint(0, 10)  

    def alimentar(self):
        self.fome -= 1
        print(f"{self.nome} foi alimentado!")

    def brincar(self):
        self.tedio -= 1
        print(f"{self.nome} brincou e está mais feliz!")

    def ouvir(self):
        print(f"{self.nome} está feliz em conversar com você!")


fazenda = [Bichinho("Cachorro"), Bichinho("Gato"), Bichinho("Coelho")]


while True:
    print("\n--- Menu ---")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for bichinho in fazenda:
            bichinho.alimentar()
    elif opcao == "2":
        for bichinho in fazenda:
            bichinho.brincar()
    elif opcao == "3":
        for bichinho in fazenda:
            bichinho.ouvir()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Escolha novamente.")
