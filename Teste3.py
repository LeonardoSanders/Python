def miniMaxSum(arr):
    mini = arr.copy()
    maxi = arr.copy()
    
    mini.remove(max(mini))
    maxi.remove(min(maxi))

    
    return result

l = [1, 2, 3, 4, 5]
a = miniMaxSum(l)
print(a)