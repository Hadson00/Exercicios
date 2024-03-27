def operacao(num, num2):
    soma = num + num2
    subtracao = num-num2
    divisao = num/num2
    mult = num*num2
    return soma, subtracao, divisao, mult

n= int(input("Digite um número: "))
n2= int(input("Digite um número: "))
print(operacao(n, n2))