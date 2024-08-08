#Métodos úteis dos dicionários em Python
def espaco():
    print()
    print('-'*50)
    print()

#len - retorna a quantidade de chaves:
pessoa = {
    'nome': 'Leo Sanders',
    'idade': '29',
    'altura': '1.83',
    'Profissão': 'Programador'
}

print(len(pessoa))
# ou
print(pessoa.__len__())
espaco()

#Keys - iterável com chaves
#Pode ser convertido em Tupla ou Lista
print(pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))
espaco()

#Values - iterável com chaves
#Pode ser convertido em Tupla ou Lista
print(pessoa.values())
espaco()

#Items - iterável com chaves
#Pode ser convertido em Tupla ou Lista
print(pessoa.items())
espaco()

#setdefault - adiciona valor padrão se a chave não existir:
pessoa.setdefault('estado civil', 'Solteiro')
print(pessoa['estado civil'])