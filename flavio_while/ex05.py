n = str(input("Digite sua senha: "))
i = True

while i:
    while n.islower():
        n = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")
    while len(n) < 6 or len(n) > 12:
        n = input("A senha deve conter no minimo 6 caracter e no maximo 12: ")
    while n.isalpha():
        n = input("É necessario de pelo menos um número: ")
    while n.isalnum():
        n = input("É necessario de pelo menos um caracter: ")
    else:
        i = False