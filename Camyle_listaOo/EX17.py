from random import randint
class bichinho () :
    def __init__(self, nome, fome, saude,idade) :
       self.nome(nome)
       self.fome(fome)
       self.saude(saude)
       self.idade(idade)

    def nome (self,nome) :
        self.nome = nome
    def fome (self, fome) :
        self.fome = fome
    def saude (self, saude) :
        self.saude = saude
    def idade (self, idade) :
        self.idade = idade 
    def nome (self,nome) :
        self.nome = nome
    def fome (self, fome) :
        self.fome = fome
    def saude (self, saude) :
        self.saude = saude
    def idade (self, idade) :
        self.idade = idade 
    def humor (self) :
        return self.getfome() * self.getsaude
    def alimenta (self, quantidade) :
        if (quantidade >= 0) and (quantidade <= 100) :
            self.fome -= self.fome * (quantidade / 100)
            


    