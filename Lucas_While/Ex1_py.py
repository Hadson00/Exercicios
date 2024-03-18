def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Digite um numero: "))

if n <= 0:
    print("Pfv que seje positivo.")
else:
    result = fibonacci(n)
    print(f"Os primeiros {n} números da sequência de Fibonacci são: {result}")