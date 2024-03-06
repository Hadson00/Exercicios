n = int(input("Valor a ser encontrado na tabela Fibonacci : "))
ult=1
pnult=1
tf = 1
ix = 2
if (n==1) or (n==2):
    print("1")
else:
    print(tf)
    while ix < n:
        print(tf)
        tf = ult + pnult
        pnult = ult
        ult = tf
        ix += 1
    print(tf)