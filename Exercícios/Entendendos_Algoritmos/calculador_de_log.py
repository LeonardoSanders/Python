from math import log2
def log_calculator(num):
    #return log2(num)
    for n in range(2, num):
        log = 2 ** n
        if log >= num:
            return n


while True:
    number = input('Digite o valor inteiro de Log: ')
    try:
        number = int(number)
        break
    except:
        print('O valor digitado não é um número inteiro!')

print(f'O Log de {number} é {round(log_calculator(number))}!')