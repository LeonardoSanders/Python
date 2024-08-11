#O Set é eficiente em remover valores duplicados de iteráveis.
# - Seus valore serão sempre únicos;
# - Não aceitam valores mutáveis;
# - Não tem index;
# - Não garantem ordem;
# - São iteráveis (for, in, not in)

lista1 = [1, 2, 3, 3, 3, 3, 1]
s3 = set(lista1)
lista2 = list(s3)
print(lista2)