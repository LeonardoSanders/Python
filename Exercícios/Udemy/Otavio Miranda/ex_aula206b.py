from ex_aula206a import CAMNHIO_ARQUIVO, Pessoa
import json

with open(CAMNHIO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)