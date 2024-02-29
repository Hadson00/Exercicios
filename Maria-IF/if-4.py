s = int(input("digite o valor do salário:"))
if s < 500 :
    s = s - (s * 0.15)
    print("O reajuste foi:",s)
elif s < 1000 and s > 500 :
    s = s - ( s * 0.10)
    print("O reajuste foi:",s)
else:
    s = s - (s * 0.05)
    print("O reajuste foi:",s)