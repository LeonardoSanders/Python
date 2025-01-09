class Banco:

    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco


class Agencia(Banco):

    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero
    
    def __str__(self):
        return f'Banco: {self._nome} | Endereço: {self._endereco} | Agência: {self._numero}'



exp_1 = Agencia('Bradesco', 'Av. Paraiba, n 10', 3937)
print(exp_1)