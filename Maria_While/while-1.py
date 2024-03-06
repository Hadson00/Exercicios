n = int(input("Valor a ser encontrado na tabela Fibonacci : "))
f=1
i=1
t = 1
ix = 2
if (n==1) or (n==2):
    print("1")
else:
    print(t)
    while ix < n:
        print(t)
        t = f + i
        i = f
        f = t
        ix += 1
    print(tf)