def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

v = int(input("Digite um valor: "))

if v == 1 or v == 2:
    resultado = v ** 3
    print(f"O valor elevado ao cubo é: {resultado}")
elif v % 3 == 0:
    resultado = fatorial(v)
    print(f"O fatorial do valor é: {resultado}")
elif v == 4 or v == 5 or v == 7 or v == 8:
    resultado = v / 9
    print(f"O valor dividido por 9 é: {resultado}")
else:
    print("O valor não corresponde a nenhuma condição")