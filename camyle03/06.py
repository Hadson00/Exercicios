def agrupar_anagramas(lista_palavras):
    anagramas_dict = {}
    for palavra in lista_palavras:
        chave = tuple(sorted(palavra))
        if chave in anagramas_dict:
            anagramas_dict[chave].append(palavra)
        else:
            anagramas_dict[chave] = [palavra]
    
    return list(anagramas_dict.values())

lista_palavras = ["amor", "fado", "astro", "amigo",  "roma", "dofa", "sorta", "magio"]

lista_anagramas = agrupar_anagramas(lista_palavras)
print("Lista de listas de anagramas:")
print(lista_anagramas)