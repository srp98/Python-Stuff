# Bubble Sort
def bubble_sort(x):
    n = len(x)

    # Traverse all the elements in x
    for i in range(n):

        # Last i elements in place
        for j in range(0, n-i-1):

            # Traverse the remaining and swap elements
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]


# Testing
arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(f"Sorted array of: {arr} {bubble_sort(arr)}\n is: {list(arr[i] for i in range(len(arr)))}")
