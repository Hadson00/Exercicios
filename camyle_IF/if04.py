#11- Faça um programa em Python para encontrar a mediana de três valores inseridos pelo usuário.


numero1 = int(input("digite um numero:"))
numero2 = int(input("digite um numero:"))
numero3 = int(input("digite um numero:"))

numeros_ordenados = sorted([numero1, numero2, numero3])
mediana = numeros_ordenados[1]
print("A mediana dos números é", mediana)