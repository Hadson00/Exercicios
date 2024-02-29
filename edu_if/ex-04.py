s = float(input("Digite o salario atual: "))
if s < 500:
    r = s * 0.15
    print(s - r)
elif s > 500 and s < 1000:
    r = s * 0.10
    print(s  - r)
else:
    r = s * 0.05
    print(s - r)