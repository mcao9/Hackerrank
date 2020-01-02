import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length = len(s)
    repeats = n // length
    rem = n % length
    count = 0
    count2 = 0
    for char in s:
        if char == 'a':
            count += 1
    
    for i in range(rem):
        if s[i] == 'a':
            count2 += 1
    return repeats * count + count2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

# s, n = input().strip(), int(input().strip())
# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))