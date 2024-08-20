# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
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
#print(*novos_produtos, sep='\n')

produtos.sort(key=lambda item: item['nome'], reverse=True)
produtos_ordenados_por_nome = deepcopy(produtos)
#print(*produtos_ordenados_por_nome, sep='\n')

produtos.sort(key=lambda item: item['preco'])
produtos_ordenados_por_preco = deepcopy(produtos)
print(*produtos_ordenados_por_preco, sep='\n')