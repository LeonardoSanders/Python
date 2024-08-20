# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
#Decoradores são "Syntax Sugar" - Açúcar Sintático


#Abaixo está um exemplo de função decoradora!
def create_func(func):
    def inner_func(*args):
        for arg in args:
            check_str(arg)
            result = func(*args)
            return result
    return inner_func


@create_func
def reverse_string(string):
    return string[::-1]


def check_str(value):
    if not isinstance(value, str):
        print('Os valores informados devem ser do tipo STR!')


invertida = reverse_string('Leonardo')
print(invertida)

#O @create_func é um comando utilizado para indicar ao Python qual função será automaticamente
#passada para dentro de outra, no caso, de create_func. Reduzindo assim, a necessidade de
#criar outras variáveis para utilizar a função decoradora!