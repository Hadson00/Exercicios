t1 = int(input("digite o placar do time 1:"))
t2 = int(input("digite o placar do time 2:"))
if t2 == t1:
    print("O jogo terminou em empate")
elif t2 > t1:
    print("O Time 2 venceu o jogo")
else:
    print("O Time 1 venceu o jogo")