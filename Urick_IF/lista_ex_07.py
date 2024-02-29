i = int(input("Digite valor de i:"))
a = float(input("Digite valor de a:"))
b = float(input("Digite valor de a:"))
c = float(input("Digite valor de a:"))

if i % 2 == 0:
    media = (a + b + c) / 3
    print(f"A média aritmético de a, b e c é: {media: .2f}")
elif i > 10:
    media_ponderada = (2*a + 3*b + 4*c) / (2 + 3 + 4)
    print(f"A média ponderada de a, b e c é: {media_ponderada:.2f}")
else:
    print("Não foi possível calcular a média. Verifique os valores de i e tente novamente.")
