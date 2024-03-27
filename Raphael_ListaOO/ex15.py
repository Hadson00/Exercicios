class Tamagoshi():
    def __init__(self, Nome, Fome, Saude, Idade):
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade
    
    def inserirDados(self, Nome, Fome, Saude, Idade):
        print("--------------------------------------")
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade 
        

    def alterarDados(self, Nome, Fome, Saude, Idade):
        print("--------------------------------------")
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade 
        print("Nome: ",self.Nome)
        print("Fome: ",self.Fome)
        print("Saúde: ",self.Saude)
        print("Idade: ",self.Idade)
        humor = self.Fome + self.Saude
        print("Humor: ",humor)
    
    def alimentar(self, comida):
        self.Fome

    def __str__(self):
        return f"."

bicho = Tamagoshi("Rapha",100,100,18) 

Nome = str(input("Digite um nome: "))
Fome = int(input("Digite o nivel de fome: "))
Saude = int(input("Digite o nivel de saúde: "))
Idade = int(input("Digite sua idade: "))

bicho.inserirDados(Nome, Fome, Saude, Idade )

Nome = str(input("Digite um nome: "))
Fome = int(input("Digite o nivel de fome: "))
Saude = int(input("Digite o nivel de saúde: "))
Idade = int(input("Digite sua idade: "))
bicho.alterarDados(Nome, Fome, Saude, Idade)

