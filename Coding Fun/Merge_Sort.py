# Merge Sort
def merge_sort(x):
    # Initialize required params
    print(f'Splitting {x}')
    if len(x) > 1:
        l = len(x)
        mid = l // 2
        left = x[:mid]
        right = x[mid:]

        # Recursive for both halves
        merge_sort(left)
        merge_sort(right)

        # Base Code
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    print(f'Merging {x}')


# Test Case
a = [21, 4, 1, 3, 9, 20, 25]
merge_sort(a)
print(f"After Merge Sort: {a}")
