"""
Selection sort is an in-place comparision sorting algorithm
Hint: Find minimum and swap
Worst complexity: n^2
Average complexity: n^2
Best complexity: n^2
Space complexity: 1
"""

num_arr = [3, 1, 21, 45, 2, 6]
for i in range(len(num_arr) - 1):
    min_index = i
    for j in range(i + 1, len(num_arr) - 1):
        if num_arr[j] < num_arr[min_index]:
            min_index = j
    num_arr[i], num_arr[min_index] = num_arr[min_index], num_arr[i]

print(num_arr)
