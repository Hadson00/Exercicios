class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida): 
        self.bucho.append(comida)

    def retornar_bucho(self):
        print(f"O bucho do Macaco {self.nome} possui dentro dele: {self.bucho}")

    def digerir(self):
        comida_permitida = ["Laranja","Lasanha","Jabuticaba"]
        for i in range(len(self.bucho)):
            if self.bucho[i] in comida_permitida:
                print(f"A comida {self.bucho[i]} foi digerido no bucho do Macaco {self.nome}")
            else:
                print(f"A comida {self.bucho[i]} não foi digerido no bucho do Macaco {self.nome}, ele o vomitou")


Macaco1 = Macaco("Loco Abreu") 
Macaco2 = Macaco("Tiquinho Soares") 

Macaco1.comer("Laranja")
Macaco1.comer("Pedra")
Macaco1.comer("Lasanha")
Macaco1.retornar_bucho()
Macaco1.digerir()
Macaco2.comer("Pedra")
Macaco2.comer("Madeira")
Macaco2.comer("Jabuticaba") 
Macaco2.retornar_bucho()
Macaco2.digerir()