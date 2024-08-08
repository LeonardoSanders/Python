#Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome1'] = 'Leonardo Gomes'

print(pessoa)
print(pessoa['nome1'])

chave = 'nome2'
pessoa[chave] = 'Dandara Queiroz'
print(pessoa[chave])

#
print('-' * 50)
#

print(pessoa.get('nome1', 'Não existe!'))
print(pessoa.get('nome3', 'Não existe!'))
if pessoa.get('nome1') is not None:
    print(pessoa['nome1'])
else:
    print('Chave não existe!')