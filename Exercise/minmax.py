#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    sum_arr = []
    lenarr = len(arr)
    i = 0
    while i < lenarr:
        item = arr.pop(0)
        sum_arr.append(str(sum(arr)))
        arr.append(item)
        i = i + 1

    print(f"{min(sum_arr)} {max(sum_arr)}")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)
