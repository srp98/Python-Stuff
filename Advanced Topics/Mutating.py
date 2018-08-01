import numpy as np

# Create a new array from which we will select elements
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

b = np.array([0, 2, 0, 1])

# Select one element from each row using b's indices
print(a[np.arange(4), b])

# Mutate one element from each row of 'a' using indices of 'b'
a[np.arange(4), b] += 10
print(a)

# Boolean indexing
bool_ind = (a > 10)
print(bool_ind)

# Use boolean index array to construct rank 1 array consisting of elements of a corresponding to true values of bool_idx
print(a[bool_ind])

# Single statement of above bool_idx
print(a[a > 10])
