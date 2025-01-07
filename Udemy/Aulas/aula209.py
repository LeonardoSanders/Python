# O @classmethod é um factory method que permite utilizar uma funçao diretamente
# pela classe sem a necessidade do 'self', mas é preciso passar o argumento 'cls'
# na definiçao do método. PS: É como se fosse uma extensão do molde/Classe

class Pessoa:

    def __init__(self, nome, idade):
        self. nome = nome
        self.idade = idade


    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)
    
pessoa1 = Pessoa('Leonardo', 29)
pessoa2 = Pessoa.criar_com_50('Mario')
pessoa3 = Pessoa.criar_sem_nome(30)

print(f'{pessoa1.nome} tem {pessoa1.idade} anos.')
print(f'{pessoa2.nome} tem {pessoa2.idade} anos.')
print(f'{pessoa3.nome} tem {pessoa3.idade} anos.')