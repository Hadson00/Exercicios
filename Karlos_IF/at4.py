salario=float(input("Digite seu salario: "))

if salario <= 500:
    print("Seu reajuste foi de 15%: ", salario*1.15)
elif salario <= 1000:
    print("Seu reajuste foi de 10%: ", salario*1.10)
else:
    print("Seu reajuste foi de 5%: ", salario*1.05)