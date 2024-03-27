senha = input("Digite sua senha: ")
confirme = input("Confirme sua senha: ")
while senha != confirme:
    print("Senha incorreta")
    confirme = input("Confirme sua senha: ")
else:
    print("Senha confirmada")