CAMINHO_ARQUIVO = 'Exercícios/HackerRank/To_do_list.txt'


lista_tarefas = []
lista_desfazer = []

def pular_linha():
    print()

print('Lista de Tarefas')

while True:
    print('Selecione uma Opção: Listar[1], Adicionar [2], Retirar[3], Desfazer[4], Sair [5]')
    opc = input('-> ')
    if opc == '1':
        if not lista_tarefas:
            print('A lista está vazia!')
        else:
            pular_linha()
            print('LISTA:')
            for tarefa in lista_tarefas:
                print('- ' + tarefa)
    elif opc == '2':
        pular_linha()
        tarefa = input('Digite sua tarefa: ')
        lista_tarefas.append(tarefa)
        pular_linha()
        print('Tarefa adicionada com Sucesso')
    elif opc == '3':
        if not lista_tarefas:
            pular_linha()
            print('Não há nada para Retirar da lista...')
        else:
            pular_linha()
            print(f'Retirando {lista_tarefas[-1]} da lista...')
            lista_desfazer.append(lista_tarefas.pop())
    elif opc == '4':
        if not lista_desfazer:
            pular_linha()
            print('Não há nada para Desfazer...')
        else:
            pular_linha()
            print(f'Readicionando {lista_desfazer[-1]} na lista')
            lista_tarefas.append(lista_desfazer.pop())
    elif opc == '5':
        print('Porgrama Lista de Tarefas encerrado...')
        break
    else:
        print('Opção inválida! Tente novamente...')
    pular_linha()