def criar_func(func):
    def interna(*args):
        for arg in args:
            checagem_string(arg)
        result = func(*args)
        return f'O resulto é: {result}'
    return interna


def inverte_string(string):
    return string[::-1]


def checagem_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError(f'Este caractere {parametro} não é uma String')
    

checagem_param = criar_func(inverte_string)
inverter_palavra = checagem_param('123')
print(inverter_palavra)