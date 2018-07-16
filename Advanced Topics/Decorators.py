class Current:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """" Get the current voltage"""
        return self._voltage


class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        # when using '@instance_of_pizza' before a function def, the function gets passed onto 'topping'
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)


c1 = Current()
print(c1.voltage)

pizza = Pizza()


@pizza
def cheese():
    return 'cheese'


@pizza
def sauce():
    return 'sauce'


print(pizza)
