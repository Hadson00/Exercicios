i = True
s = 0
while i :
    n = int (input("digite um numero ou 0 para encerrar"))
    s = s + n
    if n == 0 :
        i = False
print(f"a soma dos numeros é {s}")