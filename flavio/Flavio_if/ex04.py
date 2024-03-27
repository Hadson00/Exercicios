x = float(input("Digite seu salário: "))

if x < 500:
    x = x + (x * 0.15)
elif x <= 1000:
    x = x + (x * 0.1)
else:
    x = x + (x * 0.05)

print("O salário será: ", x)