from itertools import permutations

def anagrama(palavra):
    
    subs_letras = permutations(palavra)
    lista = []
    
    for ix in subs_letras:
        nova_palavra = ''.join(ix)
        lista.append(nova_palavra)
    
    return lista


palavra = input("Digite uma palavra: ")
anagramas = anagrama(palavra)
print("Todas os anagramas possiveis:")
print(anagramas)
