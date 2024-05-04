# Mis-case
def f(x=[]):
    x.append(len(x))
    return x


print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')


# Correction
def g(x=None):
    if x is None:
        x = []
    x.append(len(x))
    return x


print(f'g() = {g()}')
print(f'g() = {g()}')
print(f'g() = {g()}')
print(f'g() = {g()}')


# Mis-Case-Wrapping Correction
def f(*args, **kwargs):
    def f(x=[]):
        x.append(len(x))
        return x
    return f(*args, **kwargs)


print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')


# Decorator Problem
def d(f):
    def _(*args, **kwargs):
        return f(*args, **kwargs)
    return _


@d
def f(x=[]):
    x.append(len(x))
    return x


print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')


# Class_Case_staticmethod
class A:
    @staticmethod
    def f(x=[]):
        x.append(len(x))
        return x


print(f'A.f() = {A.f()}')
print(f'A.f() = {A.f()}')
print(f'A.f() = {A.f()}')
print(f'A.f() = {A.f()}')

