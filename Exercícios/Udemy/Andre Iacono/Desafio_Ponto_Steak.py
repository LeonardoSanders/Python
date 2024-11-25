msg = 'Bem vindo ao verificador do ponto da carne'
print('_' * len(msg))
print(f'\n{msg}')
print('_' * len(msg))
temp = int(input('\nInforme a temperatura da carne: '))

if temp < 48:
    print('A carne está crua e precisa ficar mais tempo no fogo!')
elif temp in range(48, 54):
    print('A carne está selada. Bom apetite!')
elif temp in range(54, 60):
    print('A carne está ao ponto para mal. Bom apetite!')
elif temp in range (60, 65):
    print('A carna está ao ponto. Bom apetite!')
elif temp in range (65, 71):
    print('A carna está ao ponto para bem. Bom apetite!')
else:
    print('A carne está bem passada. Bom apetite!')