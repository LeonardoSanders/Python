#Generator expression, Iterators e Itarerables em Python
#A função do Itaretor é entregar um valor por vez, sendo sempre o próximo valor.
#Os únicos métodos presente no iterator é o next e o iter.
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
for item in iterable:
    print(next(iterator))

#O Generator não tem tamanho, indice etc, pois ele não gera e aloca os valores diretamente na memória
#Os dados serão obtidos a medida em que o Generetor for sendo requisitado
generator = (n for n in range(10000))
print(generator)

#for n in generator:
#    print(n)

#Por exemplo, na expressão acima, o Generator não gerou os 10.000 valores, mas se for executado um For Loop
#Ele retornará cada um dos 10.000 valores.
#Generator é != de Lista, que gera todos os valores e aloca diretamente na memória. Exemplo:
import sys
lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista)) #8856 bytes
print(sys.getsizeof(generator)) #192 bytes