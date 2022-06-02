from turtle import shape
import numpy as np

print(np.eye(3))
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
print(np.diag([2,2,2]))
'''
[[2 0 0]
 [0 2 0]
 [0 0 2]]
'''

num_arr = np.array([1,2,3])
print(num_arr.shape)
#output: (3,) : num_array has one dimension and it has 3 elemnents

num_arr=np.array([[1, 8, 9, 10], [12, 14, 6, 7]])
print(num_arr.shape)
#output: (2, 4) : num_array has one dimension and it has 3 elemnents