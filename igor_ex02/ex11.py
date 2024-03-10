x = int(input("Digite um valor: "))
cont = 1
valor_final = 1
if x == 1 or x == 2:
    print("o valor será: ", x**3)
elif (x % 3) == 0:
    while cont <= x:
        valor_final *= cont
        cont += 1
    print("o valor será: ", valor_final) 
elif x == 4 or x == 5 or x == 7 or x == 8:
    print("o valor será: ", x/9)
