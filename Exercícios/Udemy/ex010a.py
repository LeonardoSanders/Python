def listar(lista):
    print('\n',*lista, sep='\n')


def desfazer_lista(lista1, lista2):
    print(f'\n{lista1[-1]} removido da Lista!')
    lista2.append(lista1[-1])
    lista1.pop()


def refazer_lista(lista1, lista2):
    print(f'\n{lista2[-1]} adicionado a Lista!')
    lista1.append(lista2[-1])
    lista2.pop()

def adicionar(lista, tarefa):
    print(f'\n{tarefa} adicionado a Lista!')
    lista.append(tarefa)


todo = []
desfazer = []

while True:
    print()
    print('LISTA DE TAREFAS')
    print('[1] - Listar')
    print('[2] - Desfazer')
    print('[3] - Refazer')
    print('[0] - Sair')
    print()
    tarefa = input('Escolha uma opção ou escreva uma Tarefa: ')

    if tarefa == '0':
        print('\nSaindo da Lista de Tarefas...')
        break
   
    comandos = {
        '1': lambda: listar(todo),
        '2': lambda: desfazer_lista(todo, desfazer),
        '3': lambda: refazer_lista(todo, desfazer),
        '4': lambda: adicionar(todo, tarefa),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos.get('4')
    comando()