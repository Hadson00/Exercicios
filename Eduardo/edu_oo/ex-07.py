class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor


if __name__ == "__main__":
    
    tamagushi = Tamagushi("Tama", 10, 100, 3)

    print("Nome:", tamagushi.retornarNome())
    print("Fome:", tamagushi.retornarFome())
    print("Saúde:", tamagushi.retornarSaude())
    print("Idade:", tamagushi.retornarIdade())
    print("Humor:", tamagushi.calcularHumor())
