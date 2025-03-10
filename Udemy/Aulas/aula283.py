import os

caminho = os.path.abspath('.')

#Imprime os diretórios do caminho
for dir in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, dir)

    if not os.path.isdir(caminho_completo):
        continue
    
    #Imprime os arquivos/diretórios das pastas
    for arquivo in os.listdir(caminho_completo):
        print(arquivo)