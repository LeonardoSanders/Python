class Pessoa:
    
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'

    def aniversario(self):
        print('Feliz aniversário!')
        self.idade += 1
    
    def saudacao(self):
        return f'É um prazer conhecer um {self.profissao}'
    

p1 = Pessoa('Léo', 29, 'Programador')
print(p1)
p1.aniversario()
print(p1)
print(p1.saudacao())