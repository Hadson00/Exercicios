b = int(input("Digite quantos gols fez o Botafogo: "))
f = int(input("Digite quantos gols fez o Flamengo: "))

if b == f:
    print("Empate")
elif b > f:
    print("Vitória do Botafogo")
else:
    print("Vitória do Flamengo")