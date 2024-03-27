def par(a):
    if a % 2 == 0:
        return True
    else:
        return False

n = int(input("Digite um numero para verificar se ele é par:"))   

print(par(n))