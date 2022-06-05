# )How to find the most frequent element in a string using the max() and set( function.
# exercise from - LinkedIn group [Python Developers Community]

# The count() is a built-in function in Python. It will return the total count of a given element in a string.

input_string = "tennessee"
frequent_element = max(set(input_string), key=input_string.count)
print(frequent_element)
