def contar_letras(string):
    return len(string)

palavra = input("Digite uma palavra: ")
quantidade_letras = contar_letras(palavra)
print(f"A string possui {quantidade_letras} letras.")
