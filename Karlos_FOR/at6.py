user = input("Digite uma string: ")

reverse = ""

for char in user[::-1]:
    reverse += char
    print(reverse)