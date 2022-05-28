from functools import reduce
from itertools import chain

nested_list = [[2,4,6][8,10,12]]


print(list(chain.from_iterable(nested_list)))