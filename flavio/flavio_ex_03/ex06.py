def agrupar(lista):
    anagramas = {}
    for palavra in lista:
        chave = ''.join(sorted(palavra))
        if chave in anagramas:
            anagramas[chave].append(palavra)
        else:
            anagramas[chave] = [palavra]
    return list(anagramas.values())
print(agrupar(["listen", "silent", "enlist"]))