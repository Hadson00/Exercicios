n = float(input("Digite um número: "))
s = 0
m = 0
ix = 0
while n != 0:
    if n > 0:
        s = s + n
        ix += 1
        n = float(input("Digite um número: "))   
    else: 
        print("Número negativo, por favor digite um valor positivo")        
        n = float(input("Digite um número: "))   
m = s / ix

print("Soma final:",s)
print("Media Final:",m)