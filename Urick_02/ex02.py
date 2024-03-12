def calcular_serie(n):
    soma = 0
    for i in range(2, n + 2):
        soma += i / (i + 1)
    return soma

def obter_n_positivo():
    while True:
        n = int(input("Digite um valor positivo para n: "))
        if n > 0:
            return n
        else:
            print("O valor de n precisa ser positivo. Tente novamente.")

def main():
    n = obter_n_positivo()
    resultado = calcular_serie(n)
    print(f"O valor da série para n = {n} é: {resultado}")

if __name__ == "__main__":
    main()