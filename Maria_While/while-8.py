valor = int(input("Digite um número:"))
desc = 0
while valor != 0:
    if valor >= 1000:
        desc = valor - (valor * 0.1)
        print("O valor total com o desconto é de :", desc)
    else:
        print("O valor da compra é",valor)
    break
   