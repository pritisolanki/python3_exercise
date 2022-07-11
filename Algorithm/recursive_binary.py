def binary_recursive_search(target, arr):
    if len(arr) == 0:
        return False
    else:
        mid = (len(arr)) // 2
    print(mid, len(arr))
    if arr[mid] == target:
        return True
    else:
        if arr[mid] < target:
            return binary_recursive_search(target, arr[mid + 1 :])
        else:
            return binary_recursive_search(target, arr[:mid])


if __name__ == "__main__":
    pos = binary_recursive_search(5, [1, 2, 3, 4, 5, 6])
    print(pos)
