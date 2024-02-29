i = 1
while i != 0:
    a = int(input("Digite o valor de a: "))
    if a == 0:
        i = 0
        print("Acabaou")
    else:
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        m = (a + b + c)/3
        print("Média dos números é igual a", m)