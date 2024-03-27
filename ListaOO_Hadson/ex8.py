class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.barriga = []

    def comer(self, comida): 
        self.barriga.append(comida)

    def verBucho(self):
        print(f'O bucho do Macaco {self.nome}:\n {self.barriga}')

    def digerir(self):
        comida_permitida = ['banana','pera','manga', 'limão', 'abacaxi', 'laranja']
        for i in range(len(self.barriga)):
            if self.barriga[i] in comida_permitida:
                print(f'{self.barriga[i]} foi digerido pelo Macaco {self.nome}')
            else:
                print(f'{self.barriga[i]} não foi digerido pelo Macaco {self.nome}')

Macaco1 = Macaco('Dudu') 
Macaco2 = Macaco('Raphael') 

Macaco1.comer('abacaxi')
Macaco1.comer('limão')
Macaco1.comer('pera')
Macaco1.verBucho()
Macaco1.digerir()
print('\n')
Macaco2.comer('banana')
Macaco2.comer('laranja')
Macaco2.comer('manga')
Macaco2.comer(Macaco1.nome)
Macaco2.verBucho()
Macaco2.digerir()