# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_classe(self):
        print(self.__class__.__name__)

    def falar_nome_sobrenome(self):
        print(self.nome, self.sobrenome)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

aluno1 = Aluno("Léo", "Sanders")
cliente1 = Cliente("Joao", "Pedrosa")

cliente1.falar_classe()
aluno1.falar_nome_sobrenome()