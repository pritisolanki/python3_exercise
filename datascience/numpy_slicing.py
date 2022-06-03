# Understanding the indexing and slicing in matrix - By Priti
import numpy as np

data = np.array([[1, 2, 9], [3, 4, 8], [5, 6, 7], [4, 5, 6]])
# pick three rows
print(data[0:3])
"""
[[1 2 9]
 [3 4 8]
 [5 6 7]]
"""
# create rows by picking index 1
print(data[0:3, 1])
"""
[2 4 6]
"""
# create matrix by picking cols index from 0 to 2
print(data[0:3, 0:2])
# output
"""
[[1 2]
 [3 4]
 [5 6]]
"""
