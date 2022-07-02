#!/bin/python3

import os
import random
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference(arr):
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(0, len(arr)):
        ls_index = (len(arr) - i) - 1
        for j in range(0, len(arr[i])):
            if i == j:
                diagonal_1 += int(arr[i][j])

            if j == ls_index:
                diagonal_2 += int(arr[i][j])
    return abs(diagonal_1 - diagonal_2)


if __name__ == "__main__":
    n = 3

    arr = []

    for _ in range(n):
        arr.append(list(input().rstrip().split()))
    result = diagonalDifference(arr)
    print(result)
