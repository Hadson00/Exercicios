class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"O valor a ser pago é R$ {valor_pagar:.2f}.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


if __name__ == "__main__":
    tipo_combustivel = input("Informe o tipo de combustível: ")
    valor_litro = float(input("Informe o valor por litro: "))
    quantidade_combustivel = float(input("Informe a quantidade de combustível na bomba (em litros): "))

    bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

    while True:
        print("\nMenu:")
        print("1. Abastecer por valor")
        print("2. Abastecer por litro")
        print("3. Alterar valor do litro")
        print("4. Alterar tipo de combustível")
        print("5. Alterar quantidade de combustível na bomba")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor a ser abastecido: "))
            bomba.abastecer_por_valor(valor)
        elif opcao == "2":
            litros = float(input("Informe a quantidade de litros a ser abastecida: "))
            bomba.abastecer_por_litro(litros)
        elif opcao == "3":
            novo_valor = float(input("Informe o novo valor por litro: "))
            bomba.alterar_valor(novo_valor)
        elif opcao == "4":
            novo_combustivel = input("Informe o novo tipo de combustível: ")
            bomba.alterar_combustivel(novo_combustivel)
        elif opcao == "5":
            nova_quantidade = float(input("Informe a nova quantidade de combustível na bomba (em litros): "))
            bomba.alterar_quantidade_combustivel(nova_quantidade)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
