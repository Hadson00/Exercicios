valor = 1
valor_final = 0
i = True

while i:
    valor = float(input("Digite um número inteiro e positivo: "))
    if valor > 0:
        valor_final = valor_final + valor
    elif valor == 0:
        i = False
    elif valor < 0 :
        continue

if valor_final > 1000:
    valor_final = valor_final * 0.9

print(f"O valor total de compra foi: R${float(valor_final)}")