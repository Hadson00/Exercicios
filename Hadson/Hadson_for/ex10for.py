x = int(input("Digite um número: "))

for i in range(x,1,-1):
    x = x * (i-1)
    if x == 0:
        x = 1
print(x)