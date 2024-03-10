maior=None
import random
matz = [[random.randint(0, 99)for _ in range(10)] for _ in range(10)]
print("Matriz: ")
for lin in matz:
    print(lin)

for i in range(10):
    for a in range(10):
        if maior is None or matz[i][a]> maior :
            maior=matz[i][a]
print("Maior valor da matriz: ", maior-1)