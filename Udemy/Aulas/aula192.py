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


def desfazer(todolist, undolist):
    try:    
        tarefa = todolist.pop()
        print(f'\n{tarefa} removida da lista')
        undolist.append(tarefa)
    except (IndexError):
        print('\nNada a desfazer')


def refazer(undolist, todolist):
    try:
        print(f'\n{undolist[-1]} adicionada à lista')
        todolist.append(undolist[-1])
        undolist.pop()
    except (IndexError):
        print('\nNada a refazer')


def adicionar(tarefa, todolist):
    if not tarefa:
        print('Você não digitou uma tarefa!')
        return
    todolist.append(tarefa)
    print(f'\n{tarefa} adicionado à lista')
    listar(todolist)


to_do_list = []
undo_list = []

while True:
    print('\nComandos: listar[1], desfazer[2], refazer[3], sair[0]')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    if tarefa == '4':
        print(f'\nSaindo da Lista de Tarefas...')
        break

    comandos = {
        '1': lambda: listar(to_do_list),
        '2': lambda: desfazer(to_do_list, undo_list),
        '3': lambda: refazer(undo_list, to_do_list),
        '4': lambda: adicionar(tarefa, to_do_list),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['4']
    comando()
    