funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista_1 = []
lista_2 = []
lista_3 = []

def carro_noite(carro, noite):
    for pessoa in carro:
        if pessoa in noite:
            lista_1.append(pessoa)


def carro_dia(carro, dia):
    for pessoa in carro:
        if pessoa in dia:
            lista_2.append(pessoa)


def func_s_carro(func, carro):
    for pessoa in func:
        if pessoa not in carro:
            lista_3.append(pessoa)


carro_noite(tem_carro, turno_noite)
carro_dia(tem_carro, turno_dia)
func_s_carro(funcionarios, tem_carro)

print(f'Funcionários que tem carro e trabalham a noite: {lista_1}')
print(f'Funcionários que tem carro e trabalham de dia: {lista_2}')
print(f'Funcionários que não tem carro: {lista_3}')