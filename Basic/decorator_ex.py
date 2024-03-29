from decorator_output import beautify_output
from decorator_output import beautify_output_withlen
from decorator_output import addtimer


@beautify_output
def today_quote():
    print("It's a beautiful sunny day")


@beautify_output
def today_flowerquote():
    print("Bee like flower")


@beautify_output_withlen
def today_motivation(q):
    print(q)


q = "Better than a thousand hollow words, is one word that brings peace.!"
today_quote()
print(today_quote.__name__)
today_flowerquote()
print(today_flowerquote.__name__)
today_motivation(q)
print(today_motivation.__name__)


@addtimer
def sort_list(lst):
    n = len(lst)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            return


lstarr = [
    64,
    34,
    25,
    12,
    22,
    11,
    90,
    12,
    22,
    11,
    44,
    5,
    6,
    7,
    8,
    10,
    21,
    34,
    67,
    54,
    89,
    88,
    65,
    33,
    77,
    3,
    4,
    91,
    92,
    93,
    94,
]
sort_list(lstarr)
