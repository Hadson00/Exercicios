sal = int(input("Digite salário:"))
tgastosdes = int(input("Digite gastos de despesa:"))

if sal > tgastosdes:
    print("Gastos dentro do orçamento.")
elif sal < tgastosdes:
    print("Orçamento estourado.")
