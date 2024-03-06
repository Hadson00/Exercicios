par = 0
imp = 0

for x in range(1,101):
    if (x % 2) == 0:
        par = par + 1
    else:
        imp = imp + 1
print("pares: ", par)
print("impares: ", imp)
