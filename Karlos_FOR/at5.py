num = int(input("escreva um numero: "))
total = 0
for x in range(1,num+1):
    print(x)
    if x != num:
        print("+")
    total = total + x

print("total: ", total)