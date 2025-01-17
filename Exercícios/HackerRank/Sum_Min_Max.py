import math
import os
import random
import re


def miniMaxSum(arr):
    mini = arr.copy()
    maxi = arr.copy()
    
    mini.remove(max(mini))
    maxi.remove(min(maxi))

    return f'{sum(mini)} {sum(maxi)}'

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))