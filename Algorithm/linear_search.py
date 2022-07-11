def linear_search(list, target):
    """
    Returns the index position of the target if found, else return None
    """
    for index in range(0, len(list)):
        if list[index] == target:
            return index
    return None


if __name__ == "__main__":
    pos = linear_search([2, 3, 4, 5, 6, 7], 4)
    if pos is None:
        print("Not Found")
    else:
        print(f"4 is found at {pos}")
