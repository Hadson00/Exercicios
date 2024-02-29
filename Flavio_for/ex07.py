i = 0
p = 0
for y in range(1,101):
    if (y % 2) == 0:
        p = p + 1
    else:
        i = i + 1
print("quantidade de pares: ", p)     
print("quantidade de impar: ", i)