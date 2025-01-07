class Restaurante:

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'


restaurante_1 = Restaurante('Dominos', 'Pizzaria')
print(restaurante_1)