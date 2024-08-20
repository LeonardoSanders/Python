# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
#Decoradores são "Syntax Sugar" - Açúcar Sintático
def inverte_string(string):
    return string[::-1]

#Abaixo está um exemplo de função decoradora!
def create_func(func):
    def inner_func(*args):
        for arg in args:
            check_str(arg)
            result = func(*args)
            return result
    return inner_func


def check_str(value):
    if not isinstance(value, str):
        print('Os valores informados devem ser do tipo STR!')


verifact_str_type = create_func(inverte_string)
invertida = verifact_str_type('Leonardo')
print(invertida)