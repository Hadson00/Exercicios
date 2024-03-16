def valido(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False

    return not stack


string1 = str(input("Digite algo:"))
string2 = str(input("Digite algo:"))
string3 = str(input("Digite algo:"))

print(valido(string1))  
print(valido(string2))  
print(valido(string3))  
