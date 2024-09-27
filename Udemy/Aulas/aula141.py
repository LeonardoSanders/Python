#Dictionary Comprehension e Set Comprehension
produtos = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dictionary = {
    chave: valor
    for chave, valor in produtos.items()
}
#print(dictionary)

dictionary = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produtos.items()
}
#print(dictionary)

#É possível converter uma lista em dicionário se ela possuir valores que se assemelham a chave: valor

lista = [
    ['a', 'valor1'],
    ['b', 'valor2'],
    ['c', 'valor3'],
]

dc = {
    chave: valor
    for chave, valor in lista
}
#print(dc)

#Set Comprehension
set1 = {num for num in range(1, 11)}
print(set1)

#Ou
print(set(range(1, 11)))