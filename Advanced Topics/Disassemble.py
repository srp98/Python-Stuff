from dis import dis

# Try Disassembling a builtin CPython function
dis(len)  # Can't do it (Type Error)


# Disassembling a defined function
def f():
    pass
dis(f)  # Two things, Loads and Returns


def f(x, y):
    return x + y
dis(f)  # Loads x , y | Binary Add | Return Value


# Try Disassembling a class
class A:
    pass
dis(A)  # Prints nothing


# Wrap it in a function and try
def _():
    class A:
        pass
dis(_)  # Returns elaborate stuff


def _():
    def f():
        pass
dis(_)


# Global Variable
x = 10
def f():
    return x
dis(f)  # Loads a Global Variable


# Local variable
def f(x):
    return x
dis(f)  # Load_Fast meaning local Variable

# Closure Structure
def _(x=10):
    def f():
        return x
    return f
dis(_)  # Indicates cosntant

# Constant Value
def _():
    return 100
dis(_)  # returns constant


# Return a function
def _(x):
    return x()
dis(_)  # Returns a call function


# Attribute Look up
def f():
    return x.a
dis(f)  # Return a Global and attribute
