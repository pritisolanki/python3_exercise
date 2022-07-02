import operator


def filternums(list):
    pos_sum, neg_sum, zero_sum = (0, 0, 0)
    for item in list:
        if item > 0:
            pos_sum += 1
        if item < 0:
            neg_sum += 1
        if item == 0:
            zero_sum += 1

    return (
        "{0:.6f}".format(pos_sum / len(list)),
        "{0:.6f}".format(neg_sum / len(list)),
        "{0:.6f}".format(zero_sum / len(list)),
    )


def filternums1(lst):
    return [
        f"{sum(op(el, 0) / len(lst) for el in lst):0.6f}"
        for op in (operator.gt, operator.lt, operator.eq)
    ]


arr = [-4, 3, -9, 0, 4, 1]
result = filternums1(arr)
print(result)
