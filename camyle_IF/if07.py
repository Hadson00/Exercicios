#9- Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) 
#e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.

time1 = int(input("digite o numero do placar time 1:"))
time2 = int(input("digite o numero do placar time 2:"))

if time1 == time2 :
    print("o jogo terminou com empate")
elif time1 > time2 :
    print("o vencedor foi o time 1")
else :
    print("o vencedor foi o time 2")

