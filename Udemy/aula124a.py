perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    },
]
cont_acerto = 0

def func_perguntas(c=0):
    global cont_acerto
    print(f'\n{list(perguntas[c].keys())[c]}: {perguntas[c]['Pergunta']}')
    print((f'\n{list(perguntas[c].keys())[1]}:'))
    
    for i, v in enumerate(perguntas[c]['Opções']):
        print(f'{i}) {v}')
    
    resp = input('Escolha uma opção: ')
    try:
        resp = int(resp)
    except:
        print('Você errou!')
        return cont_acerto

    if resp > len(perguntas[c]['Opções']) or perguntas[c]['Resposta'] != perguntas[c]['Opções'][resp]:
        print('Você errou!')
    else:
        print('Você acertou!')
        cont_acerto += 1

func_perguntas(0)
func_perguntas(1)
func_perguntas(2)

print(f'\nParabéns! Você acertou {cont_acerto} de 3 perguntas...')