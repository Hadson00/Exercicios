print("Cadastre sua senha com os seguintes criétios: \n"
      "         *Ao menos 6 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!%@#$*)\n")
senha = str(input("Digite sua senha : "))
while senha.islower():
        senha = input("A senha deve ter pelo menos um caractere MAIúSCULO: ")
while len(senha) < 6 :
    senha = input("A senha deve ter pelo menos 6 caracteres: ")
while senha.isalpha() :
    senha = input("Necessita de um número: ")
while senha.isalnum() :
    senha = input("Necessita de um caractere especial: ")