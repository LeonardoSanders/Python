from avaliacao import Avaliacao
class Carro:
    lista_carros = []

    def __init__(self, modelo, cor, ano):
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self._ligado = False
        Carro.lista_carros.append(self)

    def __str__(self):
        return f'Modelo: {self._modelo} | Cor: {self._cor} | Ano: {self._ano} | {self.ligado}'
    
    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'

    @ligado.setter
    def ligado(self, status):
        self._ligado = status
    
    @classmethod
    def listar_carros(cls):
        for carro in cls.lista_carros:
            print(f'O carro {carro._modelo} - {carro._ano} é {carro._cor} e está {carro.ligado}')
        for ava in Avaliacao.avaliacoes:
            return f'Revista: {ava.revista} | Nota: {ava.nota}'
    
    
    def receber_avaliacao(self, revista, nota):
       avaliacao = Avaliacao(revista, nota)
       Avaliacao.avaliacoes.append(avaliacao)
    











# onix = Carro('Onix', 'Preto', 2025)
# print(onix)
# onix.ligado = True
# print(onix)