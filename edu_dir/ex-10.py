valor = int(float(input("Digite um número: ")))
if valor < 0:
	print("{} em modulo é: {}".format(valor, -1*valor))
elif valor>10:
    valor1 = int(float(input("Digite novamente um número: ")))
	
    print("A diferença de {} e {} é {}".format(valor, valor1, int(valor - valor1)))
else:
	print("{} dividido por 5 é {:.3f}".format(valor, valor / 5))