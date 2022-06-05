# Exploring Range function

list_item = range(1, 11)
# list_item.reverse()

# AttributeError: 'range' object has no attribute 'reverse' 🤔
# In Python2, range returns a list.
# In Python3, range returns a range object. (everything is object)

# Solution : Using reverse
list_item = list(range(1, 11))
list_item.reverse()
print(list_item)

# Solution : Use slicing
reversed_list = list_item[len(list_item) - 1 :: -1]
print(reversed_list)
