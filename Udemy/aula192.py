path = 'to_do_list.txt'
with open(path, 'r+', encoding='utf8') as arquivo:
    arquivo.write('LISTA DE TAREFA')
    

with open(path, 'r') as arquivo:
    print(arquivo.read())