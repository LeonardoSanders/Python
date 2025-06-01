from collections import namedtuple

pessoa = namedtuple('Pessoa', 'nome sobrenome cidade')

dados = [
    pessoa('Leonardo', 'Sanders', 'Fortaleza'),
    pessoa('Dandara', 'Queiroz', 'Belém'),
    pessoa('Heliamara', 'Gomes', 'Manaus')
]

leonardo = dados[0]
print(leonardo)