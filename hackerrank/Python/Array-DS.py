#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxVal = -float('inf')
    size = len(arr)
    for i in range(1, size-1):
        for j in range(1, size - 1):
            Sum = arr[i][j] + \
                arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + \
                arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if Sum > maxVal:
                maxVal = Sum
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
