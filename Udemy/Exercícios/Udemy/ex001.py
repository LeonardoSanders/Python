produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.3} 
    if produto['preco'] > 30 else {**produto}
    for produto in produtos
    if produto['preco'] > 20
]

for produto in novos_produtos:
    print(produto)