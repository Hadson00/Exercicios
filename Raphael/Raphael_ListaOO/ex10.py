class BombaCombustivel(): 

    def __init__(self):
        self.__tipo_combustivel = None
        self.__valor_litro = 0.0
        self.__qntdd_combustivel = 0

    def abastecer_por_valor(self, dinheiro:float)->float:
        quantidade = dinheiro / self.__valor_litro
        self.__qntdd_combustivel - quantidade
        return quantidade
    
    def abastecer_por_litro(self, litro:int):
        try:
            self.qntdd_combustivel - int(litro)
            return litro * self.valor_litro
        except:
            print("Não foi possivel abastecer, você esta ultrapassando")
            
    @property
    def tipo_combustivel(self)->str:
        return self.__tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel (self, comb:str)->None:
        try:
            self.__tipo_combustivel = str(comb)
        except:
            print("Não pode ser executado.")

    @property
    def valor_litro(self)->float:
        return self.__valor_litro
    
    @valor_litro.setter
    def valor_litro (self, x:float)->None:
        try:
            self.__valor_litro = float(x)
        except:
            print("Não pode ser executado.")
    
    @property
    def qntdd_combustivel(self)->int:
        return self.__qntdd_combustivel
    
    @qntdd_combustivel.setter
    def tipo_combustivel (self, y:int)->None:
        try:
            self.__qntdd_combustivel = int(y)
        except:
            print("Não pode ser executado.")

    