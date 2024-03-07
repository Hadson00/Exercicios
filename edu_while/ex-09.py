soma = 0
quant = 0
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    soma = soma + n
    quant = quant+ 1
print("Soma: ", soma)
print(f"Média: {soma/quant:10.2f}")