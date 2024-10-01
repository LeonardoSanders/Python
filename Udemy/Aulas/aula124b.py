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
def func_perguntas(i=0):
    global cont_acertos
    print(f'\n{list(perguntas[i])[0]}: {perguntas[i]['Pergunta']}')
    print(f'\n{list(perguntas[i])[1]}:')

    for index, valor in enumerate(perguntas[i]['Opções']):
        print(f'{index}) {valor}')

    while True:
        resposta = input('Escolha uma alternativa: ')
        try:
            resposta = int(resposta)
        except:
            print('Resposta inválida! Por favor, digite uma opção numérica!')
            continue
        if resposta >= 4:
            print('Resposta inválida! Por favor, digite uma opção válida.')
            continue
        else:
            break

    if perguntas[i]['Resposta'] == perguntas[i]['Opções'][resposta]:
        print('Você acertou :)')
        cont_acertos += 1
    else:
        print('Você errou :(')
        
    
for i in range(0, 3):
    func_perguntas(i)

print(f'\nVocê acertou {cont_acertos} perguntas!')