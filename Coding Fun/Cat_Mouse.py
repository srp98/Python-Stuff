"""
Given starting positions of cats determine which will reach the mouse first, Assuming mouse doesn't move and cats travel
at same speed. If cats arrive at same time mouse will move and escape.
"""


def cat_mouse(x, y, z):
    if abs(z-x) == abs(z-y):
        return 'Mouse C'
    if abs(z-x) < abs(z-y):
        return 'Cat A'
    else:
        return 'Cat B'


if __name__ == '__main__':
    q = int(input('Enter the Number of Queries: '))
    for _ in range(q):
        c_m = list(map(int, input('Enter the position of CatA, CatB and Mouse').rstrip().split()))
        c_a = c_m[0]
        c_b = c_m[1]
        m = c_m[2]
        print(cat_mouse(c_a, c_b, m))
