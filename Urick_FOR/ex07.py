import random
x = 0
contpar = 0
contimpar = 0
x = random.randint(1,300)
for num in range(1,x):
    print(num)
    if num % 2 == 0:
         contpar += 1
    else:
        contimpar += 1
print("Par: ",contpar)
print("Impar: ",contimpar)
   