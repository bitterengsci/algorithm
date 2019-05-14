#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
from collections import Counter

def checkMagazine1(magazine, rasom):
    if (Counter(rasom) - Counter(magazine)) == {}:
        print('Yes')
    else:
        print('No')

def checkMagazine2(magazine, note):
    flag = 'Yes'
    for item in note:
        if item in magazine:
            magazine.remove(item)
        if item not in magazine:
            flag = 'No'
    print(flag)


if __name__ == '__main__':
    # mn = input().split()
    #
    # m = int(mn[0])
    #
    # n = int(mn[1])
    #
    # magazine = input().rstrip().split()
    #
    # note = input().rstrip().split()
    magazine = ['two', 'times', 'three', 'is', 'not', 'four']
    note = ['two', 'times', 'two', 'is', 'four']
    checkMagazine1(magazine, note)
    checkMagazine2(magazine, note)

