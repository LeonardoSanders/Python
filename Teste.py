import math
import os
import random
import re


def miniMaxSum(arr):
    list_min = []
    list_max = []
    list_num1 = arr.copy()
    list_num2 = arr.copy()

    for x in range(4):
        num = max(list_num1)
        list_max.append(num)
        list_num1.remove(num)

    for i in range(4):
        num = min(list_num2)
        list_min.append(num)
        list_num2.remove(num)
    
    return f'{sum(list_min)} {sum(list_max)}'

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))