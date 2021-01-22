#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = n
    hashtag = 0
    for m in range(n):
        for h in range(space-1):
            print(' ',end='')
        space -= 1
        for g in range(hashtag+1):
            print('#',end='')
        hashtag += 1
        print('')

if __name__ == '__main__':
    n = int(input())

    staircase(n)