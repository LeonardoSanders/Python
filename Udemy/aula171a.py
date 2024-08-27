"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

#Resolução 1
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def sum_lists(list1, list2):
    return [ 
        (list1[i] + list2[i])
        for i in range(len(list2))
    ]


new_list = sum_lists(lista_a, lista_b)
print(new_list)

#Resolução 2
new_list_2 = [
    (x + y)
    for x, y in zip(lista_a, lista_b)
]
print(new_list_2)

#Resolução 3
from itertools import zip_longest as zl
new_list_3 = [
    (x + y)
    for x, y in zl(lista_a, lista_b, fillvalue=0)
]
print(new_list_3)