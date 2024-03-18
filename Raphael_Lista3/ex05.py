import secrets
import string

def gerar_senha(tam):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for ix in range(tam))
    return senha


tam = 12 
senha = gerar_senha(tam)
print("Senha gerada:", senha)
