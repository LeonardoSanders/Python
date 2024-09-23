todo = []
desfazer = []

while True:
    print()
    print('LISTA DE TAREFAS')
    print('[1] - Listar')
    print('[2] - Desfazer')
    print('[3] - Refazer')
    print('[4] - Sair')
    print()
    comando = input('Escolha uma opção ou escreva uma Tarefa: ')
    if comando == '1':
        print()
        print(*todo, sep='\n')
    elif comando == '2':
        print(f'\n{todo[-1]} removido da Lista!')
        desfazer.append(todo[-1])
        todo.pop()
    elif comando == '3':
        print(f'\n{desfazer[-1]} adicionado a Lista!')
        todo.append(desfazer[-1])
        desfazer.pop()
    elif comando == '4':
        print('\nSaindo da Lista de Tarefas...')
        break
    else:
        print(f'\n{comando} adicionado a Lista!')
        todo.append(comando)