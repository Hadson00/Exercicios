def func(n):
    cont1 = 2
    cont2 = 3
    soma = 0

    while cont1 <= n:
        soma = soma + (cont1/cont2)
        cont1 = cont1 + 1
        cont2 = cont2 + 2
    return soma

n = float(input('Digite um valor: '))

print (func(n))