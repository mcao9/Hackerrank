import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    # SLOW SOLUTION #1

    # for index, number in enumerate(arr):
    #     for number in range(index, len(arr) - 1):

        
    #     triplets.append(triplet)
    
    # indexes = [i for i in range(len(arr))]
    # c = list(combinations(indexes, 3))
    # print(c)

    # clists = list(map(list, c))
    # print(clists)

    # for f, s, t in clists:
    #     check1 = arr[f] * r == arr[s]
    #     check2 = arr[s] * r == arr[t]
    #     if check1 and check2:
    #         triplets.append((f,s,t))
    # return len(triplets)

    # FASTER but still slow enough to fail 4 (runtime errors)
    # d = {}
    # for index, num in enumerate(arr):
    #     if num not in d:
    #         d[num] = [index]
    #     else:
    #         d[num].append(index)

    # print(d)

    # triplets = []

    # for k, v in d.items():
    #     if k * r in d:
    #         indexes1 = d[k * r]
        
    #         if k * r * r in d:
    #             indexes2 = d[k * r * r]
    #             print(v, indexes1, indexes2)
    #             for i in range(len(v)):
    #                 for j in range(len(indexes1)):
    #                     for k in range(len(indexes2)):
    #                         if v[i] < indexes1[j] and indexes1[j] < indexes2[k]:
    #                             triplets.append((v[i], indexes1[j], indexes2[k]))
    # print(triplets)

    # return len(triplets)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
