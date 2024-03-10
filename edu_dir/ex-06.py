s_dig=0
m_dig=0
from random import randint
matz_10x10 = []

for lin in range(10):
    lin=[]
    for colun in range(10):
        lin.append(randint(10,50))
    matz_10x10.append(lin)

for lin_matz in matz_10x10:
    print(lin_matz)

print("Diagonal da matriz: ")
for i in range(10):
    print(matz_10x10[i][i], end="")
s_dig+= matz_10x10[0][0] + matz_10x10[1][1] + matz_10x10[2][2] + matz_10x10[3][3] + matz_10x10[4][4] + matz_10x10[5][5] + matz_10x10[6][6] + matz_10x10[7][7] + matz_10x10[8][8] + matz_10x10[9][9]
m_dig+=s_dig/9
print("Soma das diagonais: ", s_dig)
print("Media das diagonais:", m_dig)