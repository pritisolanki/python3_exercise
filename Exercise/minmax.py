#!/bin/python3

import math
import os
import random
import re
import sys
import unittest
from unittest import TestCase


def minmaxsum(arr):
    sum_arr = []
    lenarr = len(arr)
    i = 0
    while i < lenarr:
        item = arr.pop(0)
        sum_arr.append(str(sum(arr)))
        arr.append(item)
        i = i + 1
    return min(sum_arr), max(sum_arr)


if __name__ == "__main__":
    unittest.main()


class TestMinmaxsum(TestCase):
    def test_minmaxsum(self):
        arr = [1, 2, 3, 4, 5]
        print(arr)
        self.assertEqual(minmaxsum(arr), ("10", "14"))
