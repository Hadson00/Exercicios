soma = 0
cont= 0 

while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        break
    soma = soma + num
    cont = cont + 1
print("Quantidade de números digitados:", cont)
print("Soma: ", soma)
print(f"Média: ", soma/cont)    