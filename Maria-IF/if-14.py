a = float(input("Altura(cm): "))
l = float(input("Largura(cm): "))
c = float(input("Comprimento(cm): "))
ld = float(input("Consumo/dia(L): "))

ct = (a * l * c) / 1000
ld = ct // ld

if ld < 2:
    print("Classificação do consumo: Consumo elevado",ld)
    print("A capacidade total do reservatório, em litros é de",ct,"L")
elif (ld >= 2) and (ld < 7):    
    print("Classificação do Consumo: Consumo moderado",ld)
    print("A capacidade total do reservatório, em litros é de",ct,"L")
else:
    print("Classificação do Consumo: Consumo reduzido",ld)
    print("A capacidade total do reservatório, em litros é de",ct,"L")   