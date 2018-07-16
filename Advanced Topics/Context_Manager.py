from sqlite3 import connect
from contextlib import contextmanager


class temptable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        print('__enter__')
        self.cur.execute('create table points2(x int, y int)')

    def __exit__(self, *args):
        print('__exit__')
        self.cur.execute('drop table points2')


with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points2 (x, y) values(1, 1)')
        cur.execute('insert into points2 (x, y) values(1, 2)')
        cur.execute('insert into points2 (x, y) values(2, 1)')
        cur.execute('insert into points2 (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points2"):
            print(row)
        for row in cur.execute('select sum(x * y) from points2'):
            print(row)

""" There is an enter and exit in our class being executed sequentially so working like a generator, So, lets optimize 
the code using a generator"""


def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('created table')
    yield
    cur.execute('drop table points')
    print('dropped table')


class contextmanager:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.gen = temptable(self.cur)
        next(self.gen)

    def __exit__(self, *args):
        next(self.gen, None)


with connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

"""------------------------------------------------------------------------------------------------------------------"""


# Decorator Functionality
class contextmanager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, *args):
        next(self.gen_inst, None)


@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('created table')
    yield
    cur.execute('drop table points')
    print('dropped table')


with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)


# Using a library to shorten the code and convert a generator to context manager
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('created table')
    try:
        yield
    finally:
        cur.execute('drop table points')
        print('dropped table')


with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)
