import numpy as np
import pprint

# creating array
a = np.arange(0, 5)
print(a.dtype)  # to find the type of array
print(np.arange(0, 10, 2))
print(np.linspace(0, 10, num=3))
print(np.zeros((2, 2)))
print(np.ones((2, 2)))

# Understanding numpy array dimensions, total number of element and shape(i.e :dimesion,number of row and cols)
num_array = np.array(
    [
        [[0, 1, 2, 3, 5], [4, 5, 6, 7, 4]],
        [[0, 1, 2, 3, 2], [4, 5, 6, 7, 3]],
        [[0, 1, 2, 3, 5], [4, 5, 6, 7, 8]],
    ]
)

print(
    f" Dimesion :{num_array.ndim}, Total no of element: {num_array.size} and shape is {num_array.shape}"
)

# indexing & slicing
arr_1d = [2, 3, 4, 5, 6, 7]

print(arr_1d[0:3])
print(arr_1d[1:])  # items after index 0
print(arr_1d[:-1])  # reverse slicing
# print all of the values in the array that are less than 5.
print(num_array[num_array < 5])

# second largest value
print(num_array.max())
maxval = num_array.max()
x = np.unique(num_array)[-2]
print(x)
