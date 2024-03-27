v = int(input("Digite quantos gols o time do vasco fez: "))
f = int(input("Digite quantos gols o time do Flamengo fez: "))

if v == f:
    print("Empate")
elif v < f:
    print("Vitória do segundo time")
else:
    print("Vitória do primeiro time")