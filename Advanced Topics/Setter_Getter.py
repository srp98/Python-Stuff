# Getter Setter in Classes
class A:
    def __int__(self, b):
        self._b = b

    @property
    def b(self, value):
        return self._b

    @b.setter
    def b(self, value):
        if value < 0:
            return ValueError('Must be Positive')
        self._b = value


if __name__ == '__main__':
    a = A
    print(f'a.b = {a.b}')
    a.b = -100
    print(f'a.b = {a.b}')

# Getter Setter in Modules
x = 10


def get_x():
    global _a
    return _a


def set_a(value):
    global _a
    if value < 0:
        raise ValueError('Must Be Positive')
    _a = value
