#Exercício 1: Utilizei a List Comprehension para adicionar as letras do nome em uma nova
#lista e exibi-las separadas por pontos.
name = "Leonardo Sanders"
new_name = '.'.join([
    letter
    for letter in name.replace(' ', '')
])
print(new_name)

#Exercício 2: Adicione as letras agrupadas de 2 em 2:

new_name = '-'.join([
    name[index:index + 2]
    for index in range(0, len(name), 2)
])
print(new_name)

#Exercício 3: Transforme todas as letras dos nomes em Maiúsculas:
names = ['léo', 'pedro', 'carlos', 'andré']
up_names = [
    name.upper()
    for name in names
]
print(up_names)

#Exercício 4: Transforme a última letra do nome em Maiúscula
names = ['léo', 'pedro', 'carlos', 'andré']
last_letter_name = [
    name.replace(name[-1], name[-1].upper())
    for name in names
]
print(last_letter_name)

#Outra opção de solução:
names = ['léo', 'pedro', 'carlos', 'andré']
last_letter_name = [
    f'{name[:-1].lower()}{name[-1].upper()}'
    for name in names
]
print(last_letter_name)

#Exercício 5: Crie uma lista de números com seus respectivos valores ao quadrado e depois transforme em formato Flat.
numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [num_individual
        for numero in numeros
        for num_individual in numero]
print(numeros)
print(flat)