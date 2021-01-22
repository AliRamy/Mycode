#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def minimaxsum(arr):
    memo = dict()
    for item in range(0,len(arr)):
        calcluate = sum(arr) - arr[item]
        memo.update({item:calcluate})
    maxvalue = 0
    for x in memo.values():
        if x > maxvalue:
            maxvalue = x
    minivalue = memo.get(0)
    for y in memo.values():
        if y < minivalue:
            minivalue = y

    return print(minivalue, maxvalue, end=' ')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    minimaxsum(arr)
