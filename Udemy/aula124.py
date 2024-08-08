perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]


cont_acertos = 0

def func_perguntas(c=0):
    global cont_acertos
    
    print(f'\n{list(perguntas[c].keys())[c]}: {perguntas[c]['Pergunta']}')
    print(f'\n{list(perguntas[c].keys())[1]}:')

    for n in range(0, 4):
        print(f'{n}) {perguntas[c]['Opções'][n]}')

    resp = input('Escolha uma opção: ')
    try:
        resp = int(resp)

func_perguntas()