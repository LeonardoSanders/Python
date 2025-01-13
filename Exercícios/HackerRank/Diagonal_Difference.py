arr = [[1, 2, 3, 1], [4, 5, 6, 1], [9, 8, 9, 1], [3, 2, 1, 1]]

def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        print(arr[i])
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n - i - 1]

    return abs(primary_diagonal - secondary_diagonal)

result = diagonalDifference(arr)
print(result)