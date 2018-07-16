# Find a number in unsorted array
p = [1, 3, 5, 6, 7, 8, 1]
q = 2


def find_number(arr, k):
    return k in arr


print(find_number(p, q))


# Finding Odd numbers within a range
m = 3
n = 9


def odd_numbers(l, r):
    odd_list = []
    for i in range(l, r+1):
        odd_list.append(i) if i % 2 == 1 else None
    return odd_list


print(odd_numbers(m, n))
