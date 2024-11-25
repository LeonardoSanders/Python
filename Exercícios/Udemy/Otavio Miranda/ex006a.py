list_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    return [
        (l1[i], l2[i])
        for i in range(len(l1))
    ]
    

final_list = zipper(list_1, list_2)
print(final_list)
print()
print('-' * 30)
print()
print(list(zip(list_1, list_2)))