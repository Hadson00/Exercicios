total_compras = 0

while True:
    valor_produto = float(input("Digite o valor do produto (ou 0 para encerrar): "))

    if valor_produto == 0:
        break
    
    if valor_produto < 0:
        ("Valor invalido. Digite um valor positivo ")
        continue
    total_compras += valor_produto

if total_compras > 1000:
    desconto = 0.1 * total_compras
    total_compras -= desconto

print(f"Total a pagar: {total_compras} Reais")