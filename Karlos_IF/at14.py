altcm = float(input("Informe a altura do reservatório em cm: "))
largcm = float(input("Informe a largura do reservatório em cm: "))
compcm = float(input("Informe a comprimento do reservatório em cm: "))
consdia = float(input("Informe o consumo médio diario em litros/dia: "))

volume_litros = (altcm * largcm * compcm) / 1000

capacidade_total_litros = volume_litros

autonomia_dias = capacidade_total_litros / consdia

if autonomia_dias < 2:
    classificacao_consumo = "Consumo Elevado"
elif autonomia_dias >=2 and autonomia_dias <=7:
    classificacao_consumo = "Consumo Moderado"
else:
    classificacao_consumo = "Consumo Reduzido"

print(f"A capacidade total do reservatório é de {capacidade_total_litros:.2f} litros")
print(f"A autonomia do reservatório é de {autonomia_dias:.2f} dias")
print(f"A classificação do consumo é: {classificacao_consumo}")










