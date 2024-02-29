altura_cm = float(input("Informe a altura do reservatório em centímetros"))
largura_cm = float(input("Informe a largura do reservatório em centímetros"))
comprimento_cm = float(input("Informe o comprimento em centímetros: "))
consumo_litros_dia = float(input("Informe o consumo diário (em litros/dia): "))

volume_litros = (altura_cm + largura_cm + comprimento_cm) / 1000
capacidade_total_litros = volume_litros
autonomia_dias = capacidade_total_litros /consumo_litros_dia 

if autonomia_dias < 2:
    classificacao_consumo = "Consumo elevado"
elif autonomia_dias >= 2 and autonomia_dias <= 7:
    classificacao_consumo = "Consumomoderado"
else:
    classificacao_consumo = "Consumo reduzido"  

print(f"A capacidade total dos reservatório é de {capacidade_total_litros:.2f} litros.")      
print(f"A autonomia do reservatório é de {autonomia_dias:.2f} dias.")
print(f"A classificação do consumo é: {classificacao_consumo}")      
