import random

x = random.randint(1,200)
int=0
fint=0
for num in range(1,x):
    print(num)
    if num % 10 == 0:
        int +=1
    else:
        fint+=1


print("Dentro do intervalo: ", int)
print("Fora do intervalo  : ", fint)