import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    # if a sticker is farther to the left than it is supposed to be
    # positive

    # if a sticker is farther right,
    # it implies the person was affected by a bribe
    bribes = 0
    for index, sticker in enumerate(q):
        index = index + 1
        change = sticker - index
        if change >= 3:
            print("Too chaotic")
            return
        for i in range(max(sticker-2, 0), index):
            if q[i] > q[index-1]:
                bribes += 1
    print(bribes)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
