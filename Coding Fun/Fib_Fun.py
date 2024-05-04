# Fibonacci with generators :)
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


for index, x in enumerate(fib()):
    if index == 5:
        break
    print(f'{x}')


# Fib Recursive is shit!
def fib_recursive(n):
    # Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive
    sol = fib_recursive(n-2) + fib_recursive(n-1)
    return sol


# Fib with dictionaries is more efficient!
# Create a dictionary with base cases
fib_d = {0: 0, 1: 1, 2: 2}


def fib_dict(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_dict(n-2, d) + fib_dict(n-1, d)
        # Memoization
        d[n] = ans
        return ans
