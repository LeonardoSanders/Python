#Mapeamento de dados em List Comprehension
#Consiste em através da definição especificada dos dados, copiá-los para outra lista de mesmo tamanho.
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

#Está ocorrendo o mapeamento dos dados com a criação de um dicionário para receber
#os dados, no qual os preços aumentaram em R$ 5.
novos_produtos = [
    {**produto, 'preco': produto['preco'] + 5} 
    for produto in produtos
]
print(*novos_produtos, sep='\n')

#Outros tipos de mapeamentos:
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    ]
print(*novos_produtos, sep='\n')
'''
No exemplo acima, o valor do preço será aumentado em 5% caso seja maior que 20
(If condition), senão,  será adicionado no novo dicionário os valores integrais
do dicionário produtos.
Caso esse Else não esteja assim, o novo dicionário ficará com dados faltando.
'''