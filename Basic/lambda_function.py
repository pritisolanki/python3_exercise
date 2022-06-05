# Lambda function exercise
# create a lambda function that sorts the list in descending order - Priti
# case 1
from numpy import intp, number


lst = [23, 45, 56, 78, 99, 35]


def reverse_list(lst):
    return sorted(lst, reverse=True)


print(reverse_list(lst))

# case 2
print(sorted(lst, key=lambda x: x, reverse=True))


# perform list join using lambda
my_list = ["lorem", "porem", "sorem"]
joinner = " ".join(map(lambda x: x, my_list))
print(joinner)

# lambda function to add 15
subject_mark = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Social sciences", 82),
]
subject_mark.sort(key=lambda x: x[1])
print(subject_mark)

# sort cars based on model - Practiced by Priti
cars = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]
cars.sort(key=lambda x: int(x["model"]))
print(cars)

# Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
lst = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
lst = sorted(lst, key=lambda x: x[1])
print(lst)
