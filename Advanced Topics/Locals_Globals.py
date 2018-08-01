# Gives all local variables in the file
print(f'locals = {locals().keys()}')

# Gives all Global variables in the file
print(f'globals = {globals().keys()}')

# Check if globals and locals same, True
print(f'locals is globals: ? {locals() is globals()}')

# Declaration, check if changed: Nothing changed
old = locals()
x = 10
print(f'locals() - old = {set(locals()) - set(old)}')

# Declaration with Copy, Check if changed: Changes
old_1 = locals().copy()
x_1 = 10
print(f'locals() - old = {set(locals()) - set(old_1)}')

# Local Declaration
locals()['z'] = 10
print(f'z = {z}')


# Function declaration
def f(a):
    print(f'a = {a}')


f(10)


def f(a=10):
    print(f'a = {a}')


f()


def f():
    locals()['b'] = 10
    print(f'b = {b}')


f()  # Name Error


def f(c=100):
    locals()['c'] = 10
    print(f'c = {c}')


f()  # Prints 100, no effect


def f():
    globals()['d'] = 10
    print(f'd = {d}')


f()  # Prints 10


def f(x=10):
    def f():
        locals()['x'] = 1
        globals()['x'] = 100
        print(f'x = {x}')
    f()


f()  # Prints 10


def f(x=10):
    def f():
        x += 1
        print(f'x = {x}')
    f()


f()  # Gives unbound Local Error
