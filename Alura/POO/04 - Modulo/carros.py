from avaliacao import Avaliacao
class Carro:
    lista_carros = []

    def __init__(self, modelo, cor, ano):
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self._ligado = False
        self._avaliacao = []
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
            print(f'Média Avaliação: {carro.media_avaliacoes}')
    

    def listar_avaliacao(self):
        for dados in self._avaliacao:
            print(f'Revista: {dados._revista} | Nota: {dados._nota}')
    
    
    def receber_avaliacao(self, revista, nota):
       avaliacao = Avaliacao(revista, nota)
       self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qnt_notas = len(self._avaliacao)
        media_avaliacoes = round(soma_das_notas / qnt_notas, 1)
        return media_avaliacoes











# onix = Carro('Onix', 'Preto', 2025)
# print(onix)
# onix.ligado = True
# print(onix)