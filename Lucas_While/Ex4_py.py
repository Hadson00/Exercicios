senha1 = (input("Digite a primeira senha: "))

senha2 = (input("Digite a segunda senha igual a primeira: "))

while senha1 != senha2:
    print("As senhas estao erradas tente dnv")

    senha1 = (input("Digite a primeira senha novamente: "))

    senha2 = (input("Digite a segunda senha igual a primeira: "))
else:
    print("Acesso permitido")