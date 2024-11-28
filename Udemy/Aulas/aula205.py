class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa_1 = Pessoa('Léo', 29)
#print(f'Seu nome é {pessoa_1.nome} e tem {pessoa_1.idade} anos!')

print(pessoa_1.__dict__)
print(vars(pessoa_1))

#OUTRA FORMA É DESEMPACOTANDO UM DICIONARIO DENTRO DA CLASSE:

dados = {
    'nome': 'Dandara',
    'idade': 28
}

pessoa_2 = Pessoa(**dados)
print(pessoa_2.__dict__)
print(vars(pessoa_2))