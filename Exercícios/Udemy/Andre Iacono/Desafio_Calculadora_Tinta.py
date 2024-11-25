rend = int(input('Informe o rendimento da lata de tinta: '))
altura = int(input('Informe a altura da parede: '))
largura = int(input('Informe a largura da parede: '))

def cal_tinta(rend, alt, larg):
    area =  alt * larg
    qnt_tinta = area / rend
    return qnt_tinta

resultado = cal_tinta(rend, altura, largura)
print(f'Você precisará de {resultado} lata(s) de tinta para pintar essa parede!')