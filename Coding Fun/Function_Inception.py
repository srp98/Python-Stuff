# Recursive lambda functions
zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)

# Convert to Int, the function calls
to_int = lambda n: n(lambda i: i+1)(0)
