def soma(x, y):
    print(f'O resultado é: {x + y}')

def sub(x, y):
    print(f'O resultado é: {x - y}')

def mult(x, y):
    print(f'O resultado é: {x * y}')

def div(x, y):
    print(f'O resultado é: {x / y}')

def erro(comando):
    print(f'Opção {comando} inválida, tente novamente!')

print('=' * 20)
print('CALCULADORA PYTHON')
print('=' * 20)
print('\nSelecione o número da operação desejada:')
print('\n[0] - Sair \n[1] - Soma \n[2] - Subtração \n[3] - Multiplicação \n[4] - Divisão')

while True:
    comando = input('\nDigite sua opção: ')
    if comando == '0':
        print('Saindo da calculadora...')
        break

    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))

    comandos = {
        '1': lambda: soma(x, y),
        '2': lambda: sub(x, y),
        '3': lambda: mult(x, y),
        '4': lambda: div(x, y),
        '5': lambda: erro(comando),
    }
    calculadora = comandos.get(comando) if comandos.get(comando) is not None else comandos['5']
    calculadora()