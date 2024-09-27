#Dicionários são estruturas de dados do tipo par chave-valor (key-value)
#Assim como listas, são considerados dados mutáveis;

pessoa_1 = {
    'nome': 'Leonardo Gomes',
    'sobrenome': 'Sanders Moura'
}
print(pessoa_1)

pessoa_2 = dict(nome='Dandara Cristina', sobrenome='Pinheiro Queiroz')
print(pessoa_2)

pessoas = dict()

for i in range(1, 6):
    pessoas[f'Nome {i}'] = input(f'Digite o {i}° nome: ')

for chave, nome in pessoas.items():
    print(chave, '=', nome)