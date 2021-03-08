#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.

def birthdayCakeCandles(candles):
    # Write your code here
    counter = 0
    big = 0
    for candle in range(len(candles)):
        for i in range(candle + 1, len(candles)):
            if candles[candle] >= candles[i]:
                big = candles[candle]
            else:
                big = candles[i]
    for item in range(len(candles)):
        if big == candles[item]:
            counter += 1
    return print(counter)

if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    birthdayCakeCandles(candles)
