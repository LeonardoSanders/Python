from modulo.veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Modelo: {self._modelo} | Marca: {self._marca} | Portas: {self._portas} | Estado: {status}'
  