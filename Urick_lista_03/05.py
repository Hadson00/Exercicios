import random
import string

def gerador_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

comprimento = int(input("Digite o comprimento da senha desejada: "))

senha_gerada = gerador_senha(comprimento)
print("A senha gerada é:", senha_gerada)