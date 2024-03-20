class TV:
    def __init__(self, numero, volume1, volume2):
        self.numero=numero
        self.volume1=volume1
        self.volume2=volume2
    
    def canalNumero(self):
            return self.numero
    
    def aumentarVolume(self):
        if self.volume1 <100:
            self.volume1+=self.volume1
        else:
            print("Volume invalido") 

    def diminuirVolume(self):
        if self.volume2 >100:
            self.volume2-=self.volume2
        else:
            print("Volume invalido")

if __name__ == "__main__":
    