""" Exercício
Crie uma função que encontre a primeira ocorrência de número duplicado, Retorne
a duplicação considerada ou -1 se não houver números duplicados.
Exemplo:
        [1, 2, 3, 3, 2, 1] --> 1, 2 e 3 estão duplicados, porém, a primeira ocorrência
        de duplicação é do número 3.
        [1, 2, 3, 4, 5, 6] --> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, 9, 4, 8] --> Retorne 9.
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def func_numero_duplicado(lista):
        comparador = set()

        for numero in lista:
            if numero in comparador:
                print(f'O número {numero} está duplicado!')
                break
            comparador.add(numero)

        if len(comparador) == len(lista):
            print('Não há números duplicados!')
        

for lista in lista_de_listas_de_inteiros:
        print(lista)
        func_numero_duplicado(lista)