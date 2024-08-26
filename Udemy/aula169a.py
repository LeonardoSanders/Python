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
full_list = []

position = 0
for city in list_cities:
    full_list.append(city)
    full_list.append(list_abbre[position])
    position += 1

print(full_list)