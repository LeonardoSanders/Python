import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()

    '''
    O código acima é uma das formas de resolver o exercício da Aula 192.
    Além disso, existe um conceito importante nisso que é o recurso de evitar o uso de
    condicionais no código. Na proposta, foi criado um dicionário com todas as opções dos comandos.
    Porém, se a função fosse chamada diretamente na criação do Dicionário, ocorreria um problema, por isso,
    foi utilizado a função genérica lambda que faz com que as funções não sejam executadas na criação
    desse dicionário.
    Na sequência, foi utilizado o comando .get para selecionar dentro do dicionário o comando desejado e
    a execução da sua respectiva função. Porém, o if/else dentro do get serve para não buggar a função de adicionar
    Ou seja, todas vez que uma tarefa precise ser adicionada, o dicionário não buscará a chave 'adicionar' e sim
    o valor atribuido a 'adicionar' que é a própria função que adiciona uma tarefa na lista.
    Se esse trecho não estivesse presente, nada poderia ser adiciona a lista através do dicionário. 
    '''