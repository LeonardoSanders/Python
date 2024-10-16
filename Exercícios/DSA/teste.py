from functools import reduce
produtos = [
    {'nome': 'Banana', 'preco': 3.5},
    {'nome': 'Maçã', 'preco': 2.0},
    {'nome': 'Laranja', 'preco': 1.5}
]

# Filtrar produtos com preço maior que 2 reais
produtos_caros = filter(lambda p: p['preco'] >= 2, produtos)

# Calcular o preço total dos produtos caros
preco_total = reduce(lambda total, p: total + p['preco'], produtos_caros, 0)

print(preco_total)