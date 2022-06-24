from itertools import product

# Combinatoric iterators  - product (by Priti)
flower = ["lily", "rose", "jasmine"]
color = ["white", "yellow"]

# mix n match flower and their available colors
print(list(product(flower, color)))
