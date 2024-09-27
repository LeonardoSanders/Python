import os
lista = []
while True:
    print('Selecione uma opção')
    opc = input('[i]nserir [a]pagar [l]istar [s]air: ')
    if opc == 'i':
        os.system('cls')
        lista.append(input('Valor: '))
        print('Item adicionado com sucesso...')
    elif opc == 'a':
        os.system('cls')
        for i, nomes in enumerate(lista):
                 print(i, nomes)
        indice = input('Escolha um índice para apagar: ')
        try:
            indice = int(indice)
            del lista[indice]
        except:
            print('Não é possível apagar esse índice!')
            continue
        else:
             print('Item apagado com sucesso!')
    elif opc == 'l':
            os.system('cls')
            for i, nomes in enumerate(lista):
                 print(i, nomes)
    elif opc == 's':
        print('Saindo do programa...')
        os.system('cls')
        break
    else:
         print('Por favor, insira uma opção válida!')
