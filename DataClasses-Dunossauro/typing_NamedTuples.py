from typing import NamedTuple, Dict

class Pessoa(NamedTuple):
    name: str
    sobrenome: str
    telefone: Dict[str, str]
    ddd: int


leonardo = Pessoa('Leonardo', 'Sanders', {'cel1': '984988513', 'cel2': '982329590'}, 92)
for dados in leonardo:
    print(dados)

'''mypy: biblioteca do python que roda testes de validação de tipagem de dados nos códigos'''