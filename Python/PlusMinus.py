#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusminus(arr):
    positive = 0
    negative = 0
    zero = 0
    if n > len(arr):
        return 'Error'
    elif n < len(arr):
        return 'Error happen'
    for item in range(0,len(arr)):
        if arr[item] > 0:
            positive = positive + 1
        elif arr[item] < 0:
            negative = negative + 1
        elif arr[item] == 0:
            zero = zero + 1

    return print(f"{format((positive/n),'.6f')}\n{format((negative/n),'.6f')}\n{format((zero/n),'.6f')}")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusminus(arr)
