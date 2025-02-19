import os
import shutil

#Salva o diretorio do usuario
HOME = os.path.expanduser('~')

#Salva o diretorio onde estão as pastas
DOCUMENTS = os.path.join(HOME, 'Documents')

#Salva o diretorio da pasta original
PASTA_ORIGINAL = os.path.join(DOCUMENTS, 'exemplo')

#E salva o diretório da pasta para onde irão os arquivos
NOVA_PASTA = os.path.join(DOCUMENTS, 'nova-pasta')

#Cria a pasta se ainda não existir
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):

    #Para criar as subpastas no local de destino:
    '''
    for dir_ in dirs:
    caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
    os.makedir(caminho_novo_diretorio, exist_ok=True)
    '''

    for file_ in files:
        #Salva o caminho original do arquivo a ser copiado
        caminho_arquivo_original = os.path.join(root, file_)

        #Salva o novo caminho para onde os arquivos serão copiados
        caminho_novo_arquivo = os.path.join(NOVA_PASTA, file_)

        #Se houverem várias pastas e arquivos, pode ser feito da seguinte forma:
        #caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_)

        #Copia os arquivos de uma pasta para outra um por vez
        shutil.copy(caminho_arquivo_original, caminho_novo_arquivo)