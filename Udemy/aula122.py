#copy - retorna uma copia raza:
#Faz com que items mutáveis como listas não sejam realmente copiadas,
# mas sim, vinculadas entre os dois dicionários.
#Isso quer dizer que se for modificado um elemento de uma Lista dentro de
#um dicionário, ocorrerá a mesma mudança no dicionário que recebeu a cópia.

dicionario_1 = {
    'num_1': 1,
    'num_2': 2,
    'lista_1': [0, 1, 2]
}

dicionario_2 = dicionario_1.copy()
dicionario_2['num_1'] = 1000
dicionario_2['lista_1'][1] = 999

print(dicionario_1)
print(dicionario_2)
print()

# Porém, é possível importar uma biblioteca em Python que nos permite fazer uma 
# cópia profunda (Deep Copy), e dessa forma, as listas e demais elementos mutáveis 
# não estão mais linkadas pelos dicionários.

import copy

dicionario_3 = {
    'num_1': 1,
    'num_2': 2,
    'lista_1': [0, 1, 2]
}

dicionario_4 = copy.deepcopy(dicionario_3)
dicionario_4['num_1'] = 1000
dicionario_4['lista_1'][1] = 999

print(dicionario_3)
print(dicionario_4)