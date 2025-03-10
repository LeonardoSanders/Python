import os
import shutil

#Salva o diretorio do usuario
HOME = os.path.expanduser('~')
print(HOME)

#Salva o diretorio onde estão as pastas
DOCUMENTS = os.path.join(HOME, 'Documents')

#Salva o diretorio da pasta original
PASTA_ORIGINAL = os.path.join(DOCUMENTS, 'Leo_Sanders')

#E salva o diretório da pasta para onde irão os arquivos
NOVA_PASTA = os.path.join(DOCUMENTS, 'nova-pasta')

#Copia direto todos os arquivos de uma pasta para outra
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

#Renomear/Mover -> shutil.move ou os.rename
shutil.move(NOVA_PASTA, NOVA_PASTA + '1')

#Remove a pasta recursivamente - Primeiro apaga a subpastas e depois a pasta principal
shutil.rmtree(NOVA_PASTA, ignore_errors=True)