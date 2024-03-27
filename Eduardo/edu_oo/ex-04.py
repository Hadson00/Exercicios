class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, altura:float)->None:
        self.nome = nome
        self.altura = altura
        self.__peso = peso
        self._idade = idade

    def envelhecer(self)->None:
        self._idade +=1
        self.crescer()

    def crescer(self)->None:
        if self._idade < 21:
            self.altura += 0.05
        elif self._idade < 26 and self._idade > 21:
            self.altura +=0.01
        else:
            self.altura -= 0.01          
    
    def engordar(self, grama:float)->None:
        self.__peso += grama

    def emagrecer(self, grama:float)->None:
        self.__peso -= grama 

    def __str__(self):
        return f"Eu sou o {self.nome} tenho {self._idade} anos com {self.__peso}Kg e {self.altura}m."

    def peso(self)->float:
        return self.__peso


edu = Pessoa("Eduardo", 19, 1.90, 83)
print(edu)
edu.envelhecer()
edu.envelhecer()
edu.engordar(0.600)
edu.envelhecer()
print(edu)
edu.envelhecer()
edu.engordar(1.600)
print(edu)
edu.envelhecer()
edu.envelhecer()
edu.envelhecer()
edu.emagrecer(0.300)
edu.envelhecer()
edu.envelhecer()
edu.emagrecer(0.200)
print(edu)

