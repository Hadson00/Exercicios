v = float(input("Digite um valor: "))

if v < 0:
    resultado = abs(v)
    print(f"O módulo do valor é: {resultado}")
elif v > 10:
    n_v = float(input("Digite outro valor: "))
    dif = n_v - v
    print(f"A diferença entre os valores é: {dif}")
else:
    resultado = v / 5
    print(f"O valor dividido por 5 é: {resultado}")