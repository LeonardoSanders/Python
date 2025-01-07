class Carro:

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}'


onix = Carro('Onix', 'Preto', '2025')
print(onix)