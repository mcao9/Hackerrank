import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    currentStatus = 0
    previousStatus = 0
    valley = 0
    for step in s:
        previousStatus = currentStatus
        if step == 'U':
            currentStatus += 1
        else:
            currentStatus -= 1

        if previousStatus < 0 and currentStatus == 0:
            valley += 1  
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()