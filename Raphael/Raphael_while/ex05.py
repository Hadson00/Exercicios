import re
while True:
    senha = input("Digite a senha: ")
    
    if len(senha) < 6 or len(senha) > 12:
        print("Senha inválida. A senha deve ter no mínimo 6 e no máximo 12 caracteres.")
        continue
    if not re.search(r"[a-z]", senha):
        print("Senha inválida. A senha deve conter pelo menos uma letra minúscula.")
        continue
    if not re.search(r"[A-Z]", senha):
        print("Senha inválida. A senha deve conter pelo menos uma letra maiúscula.")
        continue
    if not re.search(r"[0-9]", senha):
        print("Senha inválida. A senha deve conter pelo menos um número.")
        continue
    if not re.search(r"[$#@]", senha):
        print("Senha inválida. A senha deve conter pelo menos um dos seguintes caracteres especiais: $, #, @.")
        continue
    
    print("Senha válida.")
    break

