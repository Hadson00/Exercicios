class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.alt_Nome(Nome)
        self.alt_Fome(Fome)
        self.alt_Saude(Saude)
        self.alt_Idade(Idade)

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def get_Nome(self):
        return self.Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def get_Fome(self):
        return self.Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude

    def get_Saude(self):
        return self.Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def get_Idade(self):
        return self.Idade

    def CheckHumor(self): 
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'

    def get_Humor(self):
        return self.get_Fome() * self.get_Saude()
            
    def DarComida(self, Quantidade):
        if Quantidade >= 0 and Quantidade <= 100:
            self.Fome -= self.Fome * Quantidade / 100.0

    def brincar(self, Quantidade):
        if Quantidade >= 0 and Quantidade <= 100:
            self.Saude += self.Saude * Quantidade / 100.0

    def str(self):
        print('\nStatus')
        print('Nome:', self.get_Nome())
        print('Idade:', self.get_Idade())
        print('Fome:', self.get_Fome())
        print('Saude:', self.get_Saude())
        print('Humor:', self.get_Humor())
            
dog = Tamagushi('Eduardo')
dog.alt_Nome('Edu')
dog.alt_Fome(2)
dog.alt_Saude(20)
dog.alt_Idade(7)
dog.DarComida(20)
dog.brincar(80)

print('Nome:',dog.Nome)
print(dog.Fome,'de fome')
print(dog.Saude,'de saúde')
print(dog.Idade,'anos')
print('O bichinho',dog.CheckHumor())
dog.str()