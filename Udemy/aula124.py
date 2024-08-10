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

    for index, valor in enumerate(perguntas[c]['Opções']):
        print(f'{index}) {valor}')

    resp = input('Escolha uma opção: ')
    try:
        resp = int(resp)
    except:
        print('Resposta errada!')
        return cont_acertos

    if resp > len(perguntas[c]['Opções']) or perguntas[c]['Resposta'] != perguntas[c]['Opções'][resp]:
        print('Você errou!')
    else:
        print('Você acertou!')
        cont_acertos += 1

for c in range(0, 3):
    func_perguntas(c)

print(f'Você acertou {cont_acertos} perguntas!')