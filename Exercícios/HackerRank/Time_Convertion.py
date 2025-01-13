
import math
import os
import random
import re
import sys

def timeConversion(s):
    time = s[:2]
    period = s[8:10]
    minute = s[2:8]
    final_time = ''
    
    if period == 'PM' and time != '12':
        time = int(time) + 12
        if time == 24:
            time = '00'
    elif period == 'AM' and time == '12':
        time = int(time) - 12
        if time == 0:
            time = '00'


    final_time = str(time) + minute
    return final_time

    



print(timeConversion('12:45:54PM'))

# if __name__ == '__main__':
#     fptr = open(os.environ['Exercícios/HackerRank.txt'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()