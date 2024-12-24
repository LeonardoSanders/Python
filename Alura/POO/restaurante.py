class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


    

restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'
restaurante_praca.nome = 'Bistrô'

print(restaurante_praca.nome)
print(f'Restaurante ativo: {restaurante_praca.ativo}')

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print(restaurante_pizza.categoria)
print(restaurante_pizza.nome)