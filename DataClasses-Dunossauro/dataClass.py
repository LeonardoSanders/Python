from typing import Dict
from dataclasses import asdict, dataclass, field

@dataclass
class Pessoa():
    nome: str
    sobrenome: str
    ddd: int = field(repr=False)
    telefone: Dict[str, str] = field(default_factory=dict)
    nome_completo: str = field(init=False)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


leonardo1 = Pessoa('Leonardo', 'Sanders', {'cel1': '984988513', 'cel2': '982329590'}, 92)
leonardo2 = Pessoa('Leonardo', 'Gomes', 92)


# print(leonardo1 == leonardo2)
print(leonardo1.nome)
print(leonardo1.nome_completo)
leonardo2.telefone = {'movel': '92'}
print(leonardo2)

pessoa_dict = asdict(leonardo1)
print(pessoa_dict)