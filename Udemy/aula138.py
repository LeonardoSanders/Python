#Filtro de dados em List Comprehension
#É a condição alocada à direita dor For Loop
#Só entrarão na Lista aqueles dados que satisfaçam a condição.
lista = [n for n in range(10) if n < 5]
print(lista)