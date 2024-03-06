i = True
total = 0
desc = 0

while i:
    num = float(input("Produtos comprados por clientes(Valor): "))
    if num < 0:
        continue
    if num > 0 and num < 1000:
        total = total + num
    elif num >= 1000:
        desc = num * 0.1
        total = (total + num) - (desc)
    elif num == 0:
        print(f"Valor total a pagar: {total}")
        i = False

