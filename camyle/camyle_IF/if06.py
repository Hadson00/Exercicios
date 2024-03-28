#10-  Escreva um programa Python para verificar se uma letra do Alfabeto(Abecedário)
# é uma vogal ou consoante.



letra = input("digite uma letra:")
letra = letra.lower()
if letra in ['a','e','i', 'o', 'u']:
    print("a letra inserida é uma vogal")
else :
    print("a letra inserida é uma consoante")