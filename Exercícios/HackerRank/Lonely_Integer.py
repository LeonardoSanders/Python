a = [1, 2, 3, 4, 3, 2, 1]

def lonelyinteger(a):
    cont_unique = 0
    for num in a:
        cont_temp = a.count(num)
        if cont_temp == 1:
            cont_unique = num
    return cont_unique

result = lonelyinteger(a)
print(result)