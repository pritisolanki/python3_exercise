def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None


if __name__ == "__main__":
    pos = binary_search([2, 3, 4, 5, 6, 7, 8, 9], 4)
    if pos is None:
        print("Not found")
    else:
        print(f"Found number at {pos}")
