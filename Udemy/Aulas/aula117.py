#Cria funções que duplicam, triplicam e quadriplicam
#o numero recebido como parâmetro.
def func_multiplicador(multiplicador):

    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar



dobro = func_multiplicador(2)
triplo = func_multiplicador(3)
quadruplo = func_multiplicador(4)
print(dobro(5))
print(triplo(5))
print(quadruplo(5))