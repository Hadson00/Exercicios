def imc(alt, peso):
    indice = alt**2 / peso
    return indice
alt= float(input("Digite a altura em metros : "))
peso= float(input("Digite o peso kg: "))
print(imc(alt, peso))