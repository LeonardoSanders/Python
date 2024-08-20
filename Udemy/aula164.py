# Variáveis livres + nonlocal
def fora(x):
    a = x
    def dentro():
        # print(locals()) - Exibe todas as variáveis acessíveis localmente.
        return a
    return dentro

#No exemplo acima, 'a' é considerada uma variável livre pq n está definida
#dentro do escopo da função dentro().

dentro1 = fora(1)
dentro2 = fora(2)
print(dentro1())
print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

#No exemplo acima, o nonlocal permite que a variável seja de livre modificação dentro
#de determinada função. É diferente do global, que faz com que a variável tenha o mesmo
#valor dentro e fora da função. O caso do nonlocal é para tornar livre apenas dentro da função.