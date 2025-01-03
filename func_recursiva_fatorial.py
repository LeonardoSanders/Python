def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

num = 5
fat = fatorial(num)
print(fat)