from random import randint

def bin_search():
    num_right = randint(1, 10)
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    low = 0
    high = len(num_list) - 1
    while low <= high:
        half = int((low + high) / 2)
        guess = num_list[half]
        if guess == num_right:
            return f'{num_right} está na posição {half}'
        if guess < num_right:
            low = half + 1
        else:
            high = half - 1
    return None


print(bin_search())