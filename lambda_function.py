# Lambda function exercise

from audioop import reverse
from numpy import sort

#create a lambda function that sorts the list in descending order
#case 1
lst = [23, 45, 56, 78, 99, 35]
reverse_list = lambda lst: sorted(lst, reverse=True)
print(reverse_list(lst))

#case 2
lst = sorted(lst, key=lambda x: x, reverse=True)
print(lst)

#what is the pythonic way of writing lambda function case 1 OR case 2?

#perform list join using lambda
my_list = ['lorem', 'porem','sorem']
joinner = ' '.join(map(lambda x: x, my_list))
print(joinner)

