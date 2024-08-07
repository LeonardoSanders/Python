hora = input('Que horas são?: ')
try:
    hora_float = float(hora)
except:
    print('Você inseriu um horário inválido!')
else:
    if 0 < hora_float < 12:
        print('Bom dia!')
    elif 12 <= hora_float < 18:
        print('Bom tarde!')
    else:
        print('Boa noite!')
