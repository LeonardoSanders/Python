def criar_func(func):
    def interna(*args):
        for arg in args:
            verificar_str(arg)
        result = func(*args)
        return f'O restultado é: {result}'
    return interna

def inverte_string(string):
    return string[::-1]

def verificar_str(caractere):
    if not isinstance(caractere, str):
        raise TypeError('O caractere não é uma string!')


checagem_caractere = criar_func(inverte_string)
palavra_invertida = checagem_caractere('123')
print(palavra_invertida)