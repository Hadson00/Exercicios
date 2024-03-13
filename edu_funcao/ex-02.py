def numero(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

    return num

num= int(input("Digite um número: "))
print(numero(num))