def binary_search(x, l, r):
    """Finding first fault in a sequence using binary search"""
    if len(x) < 1:
        return -1

    while l < r:
        mid = (l + r) // 2
        if x[mid] == 'F':
            r = mid
        else:
            l = mid + 1
    return l if x[l] == 'F' else -1


# Test for Fault Scenario
i = ["S", "S", "S", "F", "F", "F", "F", "F", "F", "F"]
idx = binary_search(i, 0, len(i) - 1)
print(idx)


def binary_search2(arr, value):
    """Searching for a given number in an array using Binary Search"""
    l = len(arr) - 1
    r = 0
    while r <= l:
        mid = (l + r) // 2
        if arr[mid] == value:
            return f'low:{r}, mid: {mid}, high:{l}, Value Found at {mid}'
        elif arr[mid] < value:
            r = mid + 1
        else:
            l = mid - 1
    return f'low:{r}, mid: {mid}, high:{l}, Value not Found'


# Binary Search Scenario
test_arr = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 11
test_val2 = 15
print(binary_search2(test_arr, test_val1))
print(binary_search2(test_arr, test_val2))
