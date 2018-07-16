from time import sleep

# Difference between the following two add functions
def add1(x, y):
    return x + y


class Adder:
    def __call__(self, x, y):
        return x + y


class Adder2:
    def __init__(self):
        self.z = 0

    def __call__(self, x, y):
        self.z += 1
        return x + y + self.z


add2 = Adder()
print(add1(10, 20))
print(add2(10, 20))
print(type(add1), type(add2))

# Fundamentally both are same but add1 is just easier to write but Adder has more functionality which can be added later
# Lets do a demo on a scenario where you perform network requests and it needs to load data from databases


# First In-efficient Way
def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv


# Second In-Efficient Way
class Compute:
    def __call__(self, *args, **kwargs):
        rv = []
        for i in range(10):
            sleep(.5)
            rv.append(i)
        return rv


# Third Efficient Way still messy
class Compute2:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv


# Fourth Best way, To use Generators
def compute3():
    for i in range(10):
        sleep(.5)
        yield i


for val in compute3():
    print(val)
