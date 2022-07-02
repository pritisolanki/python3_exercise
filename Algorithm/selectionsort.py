"""
Selection sort is an in-place comparision sorting algorithm
Hint: Find minimum and swap
Worst complexity: n^2
Average complexity: n^2
Best complexity: n^2
Space complexity: 1
"""


def selectionsort(num_list):
    for i in range(len(num_list) - 1):
        min_index = i
        for j in range(i + 1, len(num_list) - 1):
            if num_list[j] < num_list[min_index]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]


num_list = [2, 3, 4, 1, 9, 10, 5, 18]
result = selectionsort(num_list)
print(num_list)
