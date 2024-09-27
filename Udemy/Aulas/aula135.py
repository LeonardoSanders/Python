#Empacotamento e desempacotamento de Dicionários

pessoa = {
    'nome': 'Léo',
    'sobrenome': 'Sanders'
}

#Por padrão, o desempacotamento passa os valores das chaves do dicionários.
a, b = pessoa
print(a, b)

#Porém, é possível especificar values ou items para passar valores diferentes.
a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

#Desempacotamento interno:
(a1, a2), b = pessoa.items()
print(a1, a2)
print(b)
print('-' * 50)
'''
No trecho acima, a1 e a2 vão receber 'internamente' a chave e valor do primeiro
elemento do dicionário. Ao passo que b recebe uma tupla com chave e valor juntos.
'''

#Para empacotar um dicionário:
pessoa = {
    'nome': 'Léo',
    'sobrenome': 'Sanders'
}

dados_pessoa = {
    'idade': 29,
    'altura': 1.83
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print('-' * 50)
#Kwargs - keywords arguments (argumentos nomeados)
#Utilizado para passar para funções argumentos com nomes, como os dados de um dicionário
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
print('-' * 50)
mostro_argumentos_nomeados(**pessoa_completa)