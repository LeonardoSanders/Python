funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

resultado_1 = list(tem_carro.intersection(turno_noite))
resultado_2 = list(tem_carro.intersection(turno_dia))
resultado_3 = list(funcionarios.difference(tem_carro))

print(f'Funcionários que tem carro e trabalham a noite: {resultado_1}')
print(f'Funcionários que tem carro e trabalham de dia: {resultado_2}')
print(f'Funcionários que não tem carro: {resultado_3}')