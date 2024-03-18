def contar_letra(string, letra):
    count = 0
    for char in string:
        if char == letra:
            count += 1
    return count

minha_string = input("Digite uma string: ")
minha_letra = input("Digite uma letra: ")

ocorrencias = contar_letra(minha_string, minha_letra)
print(f"A letra '{minha_letra}' aparece {ocorrencias} vezes na string '{minha_string}'.")