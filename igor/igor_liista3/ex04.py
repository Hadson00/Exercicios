def imc(kg, altura):
    result = kg / (altura * altura)
    return result

kg = float(input("Digite um peso em kilos: "))
altura = float(input("Digite uma altura em metros: "))
print("O seu imc será: ", imc(kg, altura))
