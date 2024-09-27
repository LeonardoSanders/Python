import json
#O modulo json permite utilizar as funções para criar, salvar e editar arquivos em .json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

#O trecho abaixo cria um arquivo .json passando o dict pessoa para dentro do arquivo(file).
#O comando json.dump "despeja" algo dentro do arquivo, já o json.dumps despeja apenas uma determina string para o arquivo.
with open('aula190.json', 'w', encoding='utf8') as file:
    json.dump(
        pessoa, 
        file, 
        ensure_ascii=False,
        indent=2,
    )
#O ensure_ascii=False retira a formatação padrão do json e o indent=2 faz a formatação/identação dentro do arquivo

with open('aula190.json', 'r', encoding='utf8') as file:
    pessoas = json.load(file)
    for k, v in pessoas.items():
        print(f'{k}: {v}', sep='\n')