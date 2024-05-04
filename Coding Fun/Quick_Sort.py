def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = list(filter(lambda x: x < pivot, arr))
    right = list(filter(lambda x: x > pivot, arr))
    mid = list(filter(lambda x: x == pivot, arr))
    return quick_sort(left) + mid + quick_sort(right)


print(quick_sort([6, 1, 3, 9, 11, 5, 8]))
