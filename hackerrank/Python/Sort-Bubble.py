#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swap = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swap += 1
    print('Array is sorted in', swap, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    # n = int(input())
    #
    # a = list(map(int, input().rstrip().split()))
    #
    # countSwaps(a)
    countSwaps([6, 4, 1])
