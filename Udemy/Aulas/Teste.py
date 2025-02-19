#Refazer a funćão de conversao de valores para Bytes
import math
import os
from itertools import count

def formata_tamanho(tamanho: int, base: int = 1024) -> str:
    if tamanho <= 0:
        return '0 B'
    
    index_unity = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
    i = int(math.log(tamanho, base))
    index_value = index_unity[i]
    potencia = base ** i
    result = round(tamanho/potencia, 2)

    return f'{result} {index_value}'


caminho = '/home/leosanders/Documents/Leo_Sanders'
cont = count()

for root, dirs, files in os.walk(caminho):
    the_cont = next(cont)
    # print(the_cont, root)

    # for dir_ in dirs:
    #     print('     ', the_cont, dir_)
    
    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_arquivo)
        print('     ', the_cont, file_, formata_tamanho(tamanho))