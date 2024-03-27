class Pessoa:

    def __init__(self,nome:str,idade:int,peso:float,altura:float)->None:
        self.nome = nome
        self._idade = idade
        self.__peso = peso
        self.altura = altura
    
    def envelhecer(self)->None:
        self._idade += 1
        self.crescer()

    def crescer(self)->None:
        if self._idade < 21:
            self.altura += 0.05
        elif self._idade < 50 and self._idade > 21:
            self._idade += 1
        else:
            self.altura -= 0.01    

    def engordar(self, grama:float)->None:
        self.__peso += grama

    def emagrecer(self, grama:float)->None:
        self.__peso -= grama

    def __str__(self):
        return f"Eu sou o {self.nome} tenho {self._idade} com {self.__peso}Kg e {self.altura}M."

    def peso(self)->float:
        return self.__peso

lucas = Pessoa("Lucas",19,80.120,1.80)     
print(lucas)  
lucas.envelhecer() 
lucas.envelhecer()
lucas.envelhecer()
lucas.engordar(20)
lucas.emagrecer(5)
lucas.envelhecer()
print(lucas)
