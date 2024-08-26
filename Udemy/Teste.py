from itertools import zip_longest as zl
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_c = [
    (x + y)
    for x, y in zl(lista_a, lista_b, fillvalue=0)
]
print(lista_c)