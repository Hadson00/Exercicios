valor = int(float(input("Digite um número: ")))
r=1
if valor ==1 or valor == 2:
	print("{} elevado ao quadrado é: {}".format(valor, valor ** 2))
elif valor % 3 == 0:
    for i in range(1,valor+1):
        r = r * i
    print("O fatorial de {} é {}".format(valor, r))
elif valor == 4 or valor ==5 or valor ==7 or valor ==8:
	print("{} dividido por 9 é {:.3f}".format(valor, valor / 9))
else:
    print("Valor ivalido")