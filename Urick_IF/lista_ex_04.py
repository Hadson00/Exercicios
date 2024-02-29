sal = float(input("Digite salário:"))

if sal <= 500:
    print("O reajuste no seu sálario foi de 15%", sal*1.15)
elif sal <= 1000: 
    print("O reajuste no seu sálario foi de 10%", sal*1.10)
else: 
    print("O reajuste no seu sálario foi de 5%", sal*1.05)