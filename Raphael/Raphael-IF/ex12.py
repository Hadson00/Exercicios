f = int(input("Digite um número: "))

for x in range(f,1,-1):
    f = f * (x - 1)
    
print(f)