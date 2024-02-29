numeros_pares = []

for num in range(100,401):
    num_str = str(num)
    todos_os_digitos_pares = True

    for digito in num_str:
        digito_int = int(digito)
        if digito_int % 2 != 0:
            todos_os_digitos_pares = False
            break

    if todos_os_digitos_pares:
        numeros_pares.append(num)

print(", ".join(map(str, numeros_pares)))