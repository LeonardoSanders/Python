class Carro:

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self._ligado = False

    def __str__(self):
        return f'Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano} | {self.ligado}'
    
    @property
    def ligado(self):
        return 'Carro ligado' if self._ligado else 'Carro desligado'

    @ligado.setter
    def ligado(self, status):
        self._ligado = status

onix = Carro('Onix', 'Preto', 2025)
print(onix)
onix.ligado = True
print(onix)