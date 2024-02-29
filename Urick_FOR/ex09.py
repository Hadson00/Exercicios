num_par = []

for num in range(100, 401):
    num_str = str(num)
    todos_digitos_pares = True

    for digito in num_str:
        digito_int = int(digito)
        if digito_int % 2 != 0:
            todos_digitos_pares = False
            break

    if todos_digitos_pares:
        num_par.append(num)

print(", ".join(map(str, num_par)))

