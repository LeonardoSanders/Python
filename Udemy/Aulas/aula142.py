#A função 'isinstance' é utilizado para saber se o objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, str):
        print(f'String: {item}')

    elif isinstance(item, (int, float)):
        print(f'Inteiro ou Flutuante: {item}')

    else:
        print(f'Outro: {item}')

#PS: O True aparece como int ou float pq apesar de ser do tipo boleano, ele tem valor numérico de 1