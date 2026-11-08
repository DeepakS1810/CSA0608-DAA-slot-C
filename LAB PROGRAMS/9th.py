def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = sorted([3, 4, 6, -9, 10, 8, 9, 30])

for key in (10, 100):
    position = binary_search(arr, key)
    if position != -1:
        print(f"Element {key} is found at position {position + 1}")
    else:
        print(f"Element {key} is not found")
