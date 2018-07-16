class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self, *args, **kwargs):
        pass


p1 = Polynomial(1, 2, 3)  # x^2 + 2x + 3
p2 = Polynomial(4, 8, 1)  # 4x^2 + 8x + 1
print('Representation of Polynomials-', p1, p2)
print("Adding two polynomials-", p1 + p2)
print("Degree of Polynomials-", len(p1), len(p2))
