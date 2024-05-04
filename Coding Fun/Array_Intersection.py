# Three Sorted Arrays
a = [2, 6, 9, 11, 13, 17]
b = [3, 6, 7, 10, 13, 18]
c = [4, 5, 6, 9, 11, 13]


# Intersection Function
def inter_arr(x, y, z):
    res = []
    # Tracking Indexes
    p, q, r = 0, 0, 0
    if x[p] == y[q] == z[r]:
        res.append(x[p])
        p += 1
        q += 1
        r += 1
    elif x[p] < y[q]:
        p += 1
    elif y[q] < z[r]:
        q += 1
    else:
        r += 1
    return res


print(inter_arr(a, b, c))
