matz= [0] *6
for i in range(6):
    matz[i] = [0]*6

for j in range(6):
    for a in range(6):
        matz[j][a]=int(input("Digite um número: "))

for j in range(6):
    print(matz[j])[:]

principal = [0]*6

for j in range(6):
    for a in range(6):
        if j==a:
            principal[j]=matz[j][a]

print("Principal: ",principal)