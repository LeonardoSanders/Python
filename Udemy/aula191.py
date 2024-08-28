# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

'''
Ao definir um parâmetro mutável em uma função, ex.: Lista, toda vez que a função
for chamada sem a definição da lista, será utilizada a mesma lista da definição da função.
E isso faz com que os dados sejam acumulados na mesma lista. Para evitar isso, basta definir o parâmetro mutável
como None e caso não seja fornecido o parâmetro, ele seja criado. Dessa forma, mesmo não passando a lista na chamada
da função, será criada uma nova lista e retornada. Como nos exemplos acima.
'''