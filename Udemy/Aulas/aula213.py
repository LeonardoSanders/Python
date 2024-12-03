# @property + @setter - getter e setter no modo Pythonico
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
# É importante destacar que o @property não salva o valor, ele apenas retorna.

class Caneta:

    def __init__(self, cor):
        self._cor = cor

# Private ou Protected em Python é uma convenção para tornar certas variáveis, como (_cor), protegidas, de forma que outras pessoas que forem
# utilizar o código, não manipulem tais variáveis, apenas o desenvolvedor original.


    @property
    def cor(self):
        print('PROPERTY')
        return self._cor
    

    @cor.setter
    def cor(self, valor):
        print('Estou no SETTER!', valor)
        self._cor = valor

# Ao passo que o metodo @property serve para retornar um valor de um atributo, utilizando um método. o Método @***.getter serve para
# atribuir a uma variável um determinado valor, que se comportarám como um atributo quando fora da classe, como no exemplo: caneta.cor = 'Rosa'

caneta = Caneta('Azul')
print(caneta.cor)

caneta.cor = 'Rosa'
print(caneta.cor)
