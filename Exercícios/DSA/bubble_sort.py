lista = [6, 7, 8, 3, 10, 19, 4, 1, 0]

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
    
print(lista)