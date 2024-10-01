from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_ordenados = sorted(alunos, key=lambda item: item['nota'])
print(*alunos_ordenados, sep='\n')
print()

alunos_agrupados = groupby(alunos_ordenados, key=lambda item: item['nota'])
for chave, grupo in alunos_agrupados:
    print(chave)
    for aluno in grupo:
        print(aluno)