def cal(n):
    soma = 0
    for i in range(2, (n-1) + 2):
        m = 2 * i - 1
        soma += i / m
    return soma

while True:
    n = int(input("Digite um valor positivo para n: "))
    if n > 0:
        break
    else:
        print("Por favor, digite um valor positivo.")

resultado = cal(n)
print("O valor da série para n =", n, "é:", resultado)

