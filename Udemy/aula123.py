#Pop - apaga um item com a chave especificada (tipo del) e atribui a uma variável
pessoa_1 = {
    'nome': 'Leonardo',
    'sobrenome': 'Sanders',
    'idade': 29
}

nome = pessoa_1.pop('nome')
print(nome)
print(pessoa_1)
print()

#Popitem - remove o último item do dicionário e atribui a uma variável
ultima_chave = pessoa_1.popitem()
print(ultima_chave)
print(pessoa_1)
print()

#Update - Atualiza o dicionário como um todo, modifica a chave, cria nova chave etc
pessoa_2 = {
    'nome': 'Dandara',
    'sobrenome': 'Queiroz',
    'idade': 28
}

pessoa_2.update({
    'idade': 29,
    'Altura': '1.65'
})
print(pessoa_2)

#ou

pessoa_2.update(idade=30, peso=65)
print(pessoa_2)

#ou

tupla = (('idade', 29,), ('Altura', '1.65'))
pessoa_2.update(tupla)
print(pessoa_2)
