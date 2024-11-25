def create_func(func):
    def inter(*args):
        for arg in args:
            check_is_str(arg)
        return f'O resulto é: {func(*args)}'
    return inter

@create_func
def reverse_string(string):
    return string[::-1]

def check_is_str(char):
    if not isinstance(char, str):
        raise TypeError ('Não é uma string')
    

reverse_str = reverse_string('LEONARDO')
print(reverse_str)