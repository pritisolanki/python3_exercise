# Exploring reduce - By Priti
from functools import reduce

number_list = [2, 3, 4, 5, 6, 7]
# alwawys a good idea to use sum() over reduce for summing numbers
print(reduce(lambda num1, num2: num1 + num2, number_list))

# with accumulator
print(reduce(lambda num1, num2: num1 + num2, number_list, 100))
