class Tamagushi:
    def __init__(self,  nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self,novo_nome):
        self.nome = novo_nome
    
    def alterarFome(self, nova_fome):
        self.fome = nova_fome
    
    def alterarIdade(self, nova_idade):
        self.fome = nova_idade
    
    def alterarSaude(self, nova_saude):
        self.fome = nova_saude
    
if __name__ == "__main__":
    nome = input("Nome: ")
    fome = input("Fome: ")
    saude = input("Saude: ")
    idade = int(input("Idade: "))
    bichinho = Tamagushi(nome, fome, saude, idade)
    novo_nome= input("Digite o novo nome: ")
    nome == novo_nome
    print("Novo nome: ",bichinho.alterarNome(nome))
    nova_fome = input("Digite o  estado de fome do seu bichinho: ")
    nova_fome == fome
    print("Fome: ",bichinho.alterarFome(fome))
    nova_saude = input("Digite a nova saude: ")
    saude == nova_saude
    print("Saude: ",bichinho.alterarSaude(saude))
    nova_idade = int(input("Digite a nova idade: "))
    nova_idade == idade
    print("Idade: ",bichinho.alterarIdade(idade))


