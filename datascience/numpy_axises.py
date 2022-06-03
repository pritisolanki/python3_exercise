import numpy as np

apple_price = np.array([[20, 21, 10], [20, 12, 11], [50, 23, 12]])


print(apple_price.min(axis=0))
print(apple_price.min(axis=1))

# find unique states which are selling apples
locations = {1: "New Jersey", 2: "Boston", 3: "New York", 4: "Virginia", 5: "Florida"}

apple_selling_states = np.array(
    [
        [1, 2, 5],
        [2, 3, 5],
        [1, 2, 5],
        [1, 3, 2],
        [1, 3, 1],
        [2, 1, 1],
        [2, 3, 3],
        [3, 1, 1],
    ]
)
unqiue_loc = np.unique(apple_selling_states).tolist()

get_loc = [[v for k, v in locations.items() if k == x] for x in unqiue_loc]
flatten_loc = [item for lc in get_loc for item in lc]
print(f'State selling applies are {",".join(flatten_loc[:-1])} & {flatten_loc[-1]}')
