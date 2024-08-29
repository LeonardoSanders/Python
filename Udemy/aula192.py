# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa')
        return

    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


to_do_list = []
undo_list = []

while True:
    print('\nComandos: listar[1], desfazer[2], refazer[3], sair[4]')
    comandos = input('Digite uma tarefa ou comando: ')
    if comandos == '1':
        listar(to_do_list)
        print()
        continue
    elif comandos == '2':
        try:
            tarefa = to_do_list.pop()
            print(f'\n{tarefa} removida da lista')
            undo_list.append(tarefa)
        except (IndexError):
            print('\nNada a desfazer')
    elif comandos == '3':
        try:
            print(f'\n{undo_list[-1]} adicionada à lista')
            to_do_list.append(undo_list[-1])
            undo_list.pop()
        except (IndexError):
            print('\nNada a refazer')
    elif comandos == '4':
        print(f'\nSaindo da Lista de Tarefas...')
        break
    else:
        to_do_list.append(comandos)
        print(f'\n{comandos} adicionado à lista')