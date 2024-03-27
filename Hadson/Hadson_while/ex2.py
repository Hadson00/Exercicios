def contador(n):
    return len( str(n) )
def exibe():
    n = int(input('Digite um número: '))
    print(contador(n),'dígitos')
    
while True:
    exibe()