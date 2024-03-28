usuario = input("Digite uma string:")

reverse = ""

for x in usuario[::-1]:
    reverse += x
    print(reverse)