def create_func(func):
    def exe_func(*args):
        return func(*args)
    return exe_func


@create_func
def sum(x=0, y=0):
    return x + y

receive_sum = (sum(5, 2))
print(receive_sum)