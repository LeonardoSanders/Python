from copy import deepcopy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]

novos_produtos = deepcopy(produtos)
print(*novos_produtos, sep='\n')

produtos.sort(key=lambda item: item['nome'], reverse=True)

print()
print(*produtos, sep='\n')

produtos.sort(key=lambda item: item['preco'])
print()
print(*produtos, sep='\n')