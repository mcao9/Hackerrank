import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    myHourglasses = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            topRow = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottomRow = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            myHourglasses.append(topRow + middle + bottomRow)
    return max(myHourglasses)

                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
