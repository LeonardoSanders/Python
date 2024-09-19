def create_func(func):
    def inter(*args):
        for arg in args:
            check_is_str(arg)
        result = func(*args)
        return f'O resulto é: {result}'
    return inter

@create_func
def reverse_string(string):
    return string[::-1]

def check_is_str(char):
    if not isinstance(char, str):
        raise TypeError ('Não é uma string')
    

reverse_str = reverse_string('Léo')
print(reverse_str)