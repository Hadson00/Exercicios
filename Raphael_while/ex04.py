s1 = input("Digite sua senha: ")
s2 = input("Digite sua senha novamente: ")

while s1 != s2:
    print("As senhas não correspondem. Por favor, tente novamente.")
    s1 = input("Digite sua senha: ")
    s2 = input("Digite sua senha novamente: ")

print("Senha criada com sucesso!")