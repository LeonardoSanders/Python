def plusMinus(arr):
    n = len(arr)
    posit = 0
    negat = 0
    neutro = 0
    
    for num in arr:
        if num > 0:
            posit += 1
        elif num == 0:
            neutro += 1
        else:
            negat += 1
            
    result_posit = posit / n
    result_negat = negat / n
    result_neutro = neutro / n
    
    print(f"{result_posit:.5f}")
    print(f"{result_negat:.5f}")
    print(f"{result_neutro:.5f}")



plusMinus([-1, 2, 0, -2, 3])