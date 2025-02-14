import os

#Junta as strings em uma só
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)

#Separa o diretorio (local do arquivo) do nome do arquivo
diretorio, arquivo = os.path.split(caminho)
print(diretorio)
print(arquivo)

#Separa o nome do arquivo de sua extensao
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)

#Verifica se o caminho do arquivo existe
print(os.path.exists(caminho))
print(os.path.exists('/media/leosanders/Linux/Repositórios/Python/Udemy/Aulas/aula282.py'))

#Retorna o caminho absoluto de uma pasta, no caso, da atual...
print(os.path.abspath('.'))