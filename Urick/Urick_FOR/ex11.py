import random

x = random.randint(1,200)
dentro=0
fora=0
for num in range(1,x):
    print(num)
    if num % 10 == 0:
        dentro +=1
    else:
        fora+=1


print("Dentro do intervalo: ", dentro)
print("Fora do intervalo  : ", fora)