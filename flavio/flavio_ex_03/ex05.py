import string
import random
def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))
print(gerar_senha(10))