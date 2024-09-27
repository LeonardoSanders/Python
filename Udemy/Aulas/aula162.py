# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(5))
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(2))

'''EXPLICANDO A RESOLUÇÃO
A variável 'soma_com_cinco' recebe o valor de 'criar_função', passando os argumentos
função soma e 5 (x), criar_função por sua vez tem uma função interna que recebe como
parâmetro y e retorna a função recebida por criar_função e os argumentos x e y.
Como a função interna fica armazenada dentro da variável, nenhum erro acontece, pois
sua execução foi adiada. Dessa forma, somente quando o comando print(soma_com_cinco(5)),
passando 5 como argumento de y, é dado, é quando ocorre a execução completa da função
soma que retorna x + y e o valor é exibido em tela.
O mesmo raciocício funciona para para a variável multiplica_por_dez.
'''