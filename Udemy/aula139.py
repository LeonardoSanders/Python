#List Comprehension com mais de um For:
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)

#O código acima é o equivalente ao seguinte código:
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)