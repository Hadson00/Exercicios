x = int(input("Gols do time1: "))
y = int(input("Gols do time2: "))

if x > y:
    print("Time 1 é o vencedor com", x,"gols")
elif x < y:
    print("Time 2 é o vencedor com", y,"gols") 
else: print("Empate")       