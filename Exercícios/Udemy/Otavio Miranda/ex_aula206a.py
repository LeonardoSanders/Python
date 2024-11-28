import json

CAMNHIO_ARQUIVO = 'ex-aula206.py'

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

p1 = Pessoa('Leonardo', 29)
p2 = Pessoa('Dandara', 28)
p3 = Pessoa('Gustavo', 10)

bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMNHIO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)