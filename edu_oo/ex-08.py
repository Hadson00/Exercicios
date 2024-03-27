class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        if self.bucho:
            print(f"O estômago de {self.nome} contém: {', '.join(self.bucho)}")
        else:
            print(f"O estômago de {self.nome} está vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"O estômago de {self.nome} já está vazio.")



if __name__ == "__main__":
    nome1 = input("Digite o nome do primeiro macaco: ")
    macaco1 = Macaco(nome1)

    nome2 = input("Digite o nome do segundo macaco: ")
    macaco2 = Macaco(nome2)

    print("\nAlimentando os macacos:")
    alimentos = ["banana", "maçã", "laranja"]

    for alimento in alimentos:
        macaco1.comer(alimento)
        macaco2.comer(alimento)

        macaco1.verBucho()
        macaco2.verBucho()

    print("\nOs macacos estão digerindo:")
    macaco1.digerir()
    macaco2.digerir()

    
    print(f"\n{macaco1.nome} está comendo {macaco2.nome}!")
    for alimento in macaco2.bucho:
        macaco1.comer(alimento)

    print(f"{macaco1.nome} depois de comer {macaco2.nome}:")
    macaco1.verBucho()

    print(f"{macaco2.nome} depois de ser comido:")
    macaco2.verBucho()
