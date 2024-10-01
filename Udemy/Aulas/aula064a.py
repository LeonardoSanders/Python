nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
print(f'Seu nome é {nome}')
nova_string = '*'
contador = 0
while contador < tamanho_nome:
    nova_string += f'{nome[contador]}*'
    contador += 1
print(nova_string)
