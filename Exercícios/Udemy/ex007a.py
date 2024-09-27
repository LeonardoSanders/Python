lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
def sum_list(l1, l2):
    return [
        (l1[i] + l2[i])
        for i in range(len(l2))
    ]

lista_soma = sum_list(lista_a, lista_b)
print(lista_soma)