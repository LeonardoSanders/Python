import math
lista = [12, 8, -3, 0, 1, 5, 9]

def median(list):
    numbers = list
    numbers.sort()


    median = 0
       
    if len(numbers) % 2 == 0:
        num1 = round((len(lista) / 2) - 1, 0)
        num2 = round((len(lista) / 2), 0)
        median = (num1 + num2) / 2
        return median
    else:
        median = round(int(len(lista) / 2), 0)
        return numbers[median]

        
result = median(lista)
print(result)
