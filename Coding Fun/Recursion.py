#  Simple Recursion
def recur(x):
    # Base Case of the Recursive Function
    # If less than not given falls into Infinite Recursion
    if x <= 0:
        return x
    # Recursive Function Calling and Altering Input
    return recur(x - 1)


print(recur(10))  # Recurse until 0


# Factorial using Recursion
def fact_recur(x):
    """Factorial of a number using Recursion"""
    if x < 0:
        return ValueError('Negatives are excluded!')
    if x < 2:
        return 1
    return x*fact_recur(x - 1)


print(f'Factorial of 5 is: {fact_recur(5)}')
print(f'Factorial of 5 is: {fact_recur(-2)}')


# Factorial with Iteration
def fact_iter(x):
    """Factorial of a number with Iteration"""
    if x < 0:
        return ValueError('Negatives are excluded!')
    else:
        fact = 1
        for i in range(1, x+1):
            fact *= i
        return fact


print(f'Factorial of 5 is: {fact_iter(5)}')
print(f'Factorial of 5 is: {fact_iter(-5)}')


# Fibonacci Seq. Recursion upto 'n' numbers
def fib_recur(n):
    """Fibonacci Sequence of numbers upto the given number"""
    if n == 0 or n == 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)


# Testing
print(fib_recur(5))
