# Exploring reduce - By Priti
from functools import reduce

number_list = [2,3,4,5,6,7]
print(reduce(lambda num1, num2: num1+num2,number_list))
print(reduce(lambda num1, num2: num1+num2,number_list,100))


