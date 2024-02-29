i = int(input("Digite um valor: "))

if (i % 2) == 0:
    a = int(input("Digite um valor para a: "))
    b = int(input("Digite um valor para b: "))
    c = int(input("Digite um valor para c: "))
    z = (a + b + c) / 3
    print("Media aritmetica de",a ,b ,c ,"é", z)
    if i > 10:
        z = ((a * 2) + (b * 3) + (c * 4)) / 9
        print("Media ponderada de",a ,b ,c ,"é", (f'{z:.2f}'))
else: print(i,"não é par")