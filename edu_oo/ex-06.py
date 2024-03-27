class TV:
    def __init__(self, numero, volume1, volume2):
        self.numero=numero
        self.volume1=volume1
        self.volume2=volume2
    
    def canalNumero(self):
        return self.numero
    
    def aumentarVolume(self):
        return self.volume1
    

    def diminuirVolume(self):
        return self.volume2

if __name__ == "__main__":
    while True:
        numero = int(input("Digite o número do canal: "))
        opcao = int(input("Digite: 1- para aumentar o volume | 2- para dimunuoir o volume \n"))
        if opcao == 1:
            aumentar = input("Aumente o volume: ")
            diminuir = None
        elif opcao ==2:
            diminuir = input("Diminua o volume: ")
            aumentar = None
        tv = TV(numero, aumentar, diminuir)
        print("Número do canal: ",tv.canalNumero())
        if opcao == 1:
            print("Volume aumentado para ",tv.aumentarVolume())
        elif opcao ==2:
            print("Volume diminuido para ",tv.diminuirVolume()) 
        
