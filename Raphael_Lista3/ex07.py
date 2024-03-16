def valido(s):
    lista = []
    parent = {')': '(', '}': '{', ']': '['}

    for carac in s:
        if carac in parent.values():
            lista.append(carac)
        elif carac in parent.keys():
            if not lista or parent[carac] != lista.pop():
                return False
        else:
            return False

    return not lista


string1 = str(input("Digite algo:"))
string2 = str(input("Digite algo:"))
string3 = str(input("Digite algo:"))

print(valido(string1))  
print(valido(string2))  
print(valido(string3))  
