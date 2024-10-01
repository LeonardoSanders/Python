num = input('Digite um número inteiro válido: ')
try:
    num = int(num)
except:
    print('Você inseriu um número inválido')
else:
    if num % 2 == 0:
        print(f'{num} é um número PAR!')
    else:
        print(f'{num} é um número ÍMPAR!')
