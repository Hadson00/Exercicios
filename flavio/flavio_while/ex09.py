num = 1
soma = 0
med = 0.0
quant = 0
while num != 0:
    num = int(input("Digite um número: "))
    if num == 0:
        continue
    else:
        soma += num
        quant += 1


if quant != 0:
    med = soma / quant
else:
    print("Calculo impossivel divisão por 0")

print("A soma dos números digitados é: ", soma)
print("A média dos números digitados é: ", med)