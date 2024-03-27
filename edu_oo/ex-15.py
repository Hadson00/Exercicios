class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50
    
    def alimentar(self, quantidade):
        self.fome -= quantidade * 2  
        
        if self.fome < 0:
            self.fome = 0
    
    def brincar(self, tempo):
        self.tedio -= tempo * 3  
        
        if self.tedio < 0:
            self.tedio = 0
    
    def passar_tempo(self):
        self.fome += 5
        self.tedio += 5
        
        if self.fome > 100:
            self.fome = 100
        
        if self.tedio > 100:
            self.tedio = 100
    
    def mostrar_estado(self):
        print(f"Nível de fome de {self.nome}: {self.fome}")
        print(f"Nível de tédio de {self.nome}: {self.tedio}")


bichinho = BichinhoVirtual("Fofinho")
bichinho.alimentar(3)  
bichinho.brincar(2)  
bichinho.passar_tempo()
bichinho.mostrar_estado()
