from time import time


def timer(func):
    # Wrapper
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('Elapsed is: ', after - before)
        return rv
    return f


# Higher Order Decorator
def n_times(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print('Running {.__name__}'.format(func))
                rv = func(*args, **kwargs)
            return rv
        return wrapper
    return inner


@timer
@n_times(3)
def add(x, y=5):
    return x + y


@timer
@n_times(2)
def sub(x, y=5):
    return x - y


sub = timer(sub)
print('add(10)',       add(10))
print('add(20, 40)',   add(20, 40))
print("add('a', 'b')", add("a", "b"))
print('sub(10)',       sub(10))
print('sub(20, 40)',   sub(20, 40))
print("sub('a', 'b')", sub("a", "b"))
