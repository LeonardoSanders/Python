lista = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
num_inter = 0
cont = 1

while cont <= 3:

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]

    cont += 1
    print(lista)
