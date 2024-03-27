valor = int(float(input("Digite um número: ")))

if valor >=1 and valor <= 3:
	print("{} elevado ao quadrado é: {}".format(valor, valor ** 2))
elif valor == 4 or valor == 9:
	print("A raiz quadrada de {} é {}".format(valor, int(valor ** 0.5)))
elif valor >= 6 and valor <= 8:
	print("{} dividido por 9 é {:.3f}".format(valor, valor / 9))