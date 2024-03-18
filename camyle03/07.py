def valida_parenteses(string):
    list = []
    mapeamento = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in mapeamento.values():
            list.append(char)
        elif char in mapeamento.keys():
            if not list or mapeamento[char] != list.pop():
                return False
        else:
            pass

    return not list

print(valida_parenteses("()"))
print(valida_parenteses("()[]{}")) 
print(valida_parenteses("(]"))  
print(valida_parenteses("([)]")) 
print(valida_parenteses("{[]}"))  