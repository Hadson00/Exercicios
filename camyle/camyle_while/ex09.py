s = 0
i = True
contador = 0
while i :
    v = float(input("digite  um valor inteiro ou 0 para encerrar"))
    if v != 0 :
        s = s + v
        contador += 1
    else :
        i = False
if contador > 0 :
    media = s / contador
else :
    print("Erro div por 0")
print(f"a soma é {s}  e a media é {media}")