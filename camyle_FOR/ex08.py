nome = input("Digite uma string: ")
num_letra = 0
num_digito = 0

for char in nome:
    if char.isalpha():
        num_letra += 1
    elif char.isdigit():
        num_digito += 1
print(f"A string tem {num_letra} letras e {num_digito} digitos")