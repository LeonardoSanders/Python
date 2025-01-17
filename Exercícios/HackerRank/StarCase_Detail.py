def staircase(n):
    stars = '#'
    
    for i in range(1, n+1):
        result = stars*i
        print(result.rjust(n))