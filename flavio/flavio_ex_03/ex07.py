def validar(s):
    stack = []
    mapeamento = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapeamento.values():
            stack.append(char)
        elif char in mapeamento.keys():
            if not stack or mapeamento[char] != stack.pop():
                return False
        else:
            return False
    return not stack

print(validar("(){}[]"))
print(validar("({[]})"))
print(validar("([)]"))