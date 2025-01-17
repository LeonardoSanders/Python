def miniMaxSum(arr):
    mini = arr.copy()
    maxi = arr.copy()
    result = []
    
    mini.remove(max(mini))
    maxi.remove(min(maxi))
    
    result.append(sum(mini))
    result.append(sum(maxi))
    
    return result

l = [1, 2, 3, 4, 5]
a = miniMaxSum(l)
print(a)