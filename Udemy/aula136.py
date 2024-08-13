'''
List comprehension em Python:
É uma forma rápida para criar listas a partir de iteráveis.
Basicamente é a simplificação de um For Loop em um única linha. Exemplo:
'''
lista_1 = []
for numero in range(10):
    lista_1.append(numero)
print(lista_1)

#Porém, dá pra fazer de forma mais direta e simplificada:
lista_2 = [numero for numero in range(10)]
print(lista_2)

#Outro forma de fazer o List Comprehension:
lista_3 = list(range(10))
print(lista_3)

#É importante dizer que nesse caso, o que vai ser adicionado fica a esquerda do
#argumento, ou seja, do For. E por padrão, o For Loop é executado e o numero adicionado.
#O append é feito de forma automatica e tbm é possível passar argumentos complexos:

lista_4 = [numero * 2 for numero in range(1, 10)]
print(lista_4)