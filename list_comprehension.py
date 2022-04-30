#List comprehensions provide a concise way to create lists

from numpy import number
numbers = [ x for x in range(1,31)]
print(numbers)
string = "Practice Problems to Drill List Comprehension in Your Head."

#Find all of the numbers from 1–1000 that are divisible by 8
list_8divisible = [ x for x in numbers if x%8 == 0]
print(list_8divisible)

#Find all of the numbers from numbers that have a 6 in them
list_contains6 = [ x for x in numbers if '6' in str(x)]
print(list_contains6)

#Find all of the words in a string that are less than 5 letters (use string above)
words = string.split(" ")
words_with5letters = [ word for word in words if len(word) <= 5]
print(words_with5letters)

#Use a nested list comprehension to find all of the numbers from number that are divisible by any single digit besides 1 (2-9)
result = [number for number in numbers if True in [True for x in range(3,10) if number % x == 0]]
print(result)