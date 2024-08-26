# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

list_cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_abbre = ['BA', 'SP', 'MG', 'RJ']
def zipper(list1, list2):
    return [
        (list1[i], list2[i])
        for i in range(len(list_cities))
    ]


full_list = zipper(list_cities, list_abbre)
print(full_list)

#ou

print(list(zip(list_cities, list_abbre)))

#ou

from itertools import zip_longest
print(list(zip_longest(list_cities, list_abbre, fillvalue='Sem cidade')))