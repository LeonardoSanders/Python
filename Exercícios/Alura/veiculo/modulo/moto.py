from modulo.veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Modelo: {self._modelo} | Marca: {self._marca} | Tipo: {self._tipo} | Estado: {status}'