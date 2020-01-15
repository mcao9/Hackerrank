#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    # brute force
    # t = []
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         for k in range(len(c)):
    #             if a[i] <= b[j] and b[j] >= c[k]:
    #                 t.append((a[i], b[j], c[k]))

    # return len(set(t))
    t = 0

    l1 = list(sorted(set(a)))
    l2 = list(sorted(set(b)))
    l3 = list(sorted(set(c)))

    print(l1, l2, l3)

    a1 = 0
    b1 = 0
    c1 = 0

    while(b1 < len(l2)):
        while(a1 < len(l1)) and l1[a1] <= l2[b1]:
            a1 += 1
        
        while(c1 < len(l3)) and l2[b1] >= l3[c1]:
            c1 += 1
        
        t += a1 * c1

        b1 += 1
    
    return t

                    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
