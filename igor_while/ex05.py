s = str(input("Informe sua senha: "))
ix = True
while ix:
    while s.islower():
        s = input("A senha deve conter no minimo uma letra Maiuscula: ")
    while len(s) < 6 or len(s) > 12:
        s = input("A senha deve conter no minimo 6 caracteres e no maximo 12: ")
    while s.isalpha():
        s = input("A senha deve contar numero: ")
    while s.isalnum():
        s = input("A senha deve conter caracter especial: ")
    else:
        ix = False