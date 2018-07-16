class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!!')
        self.first = None
        self.last = None


employee_1 = Employee('Shashank', 'P')
employee_1.first = 'Naveena'
employee_1.fullname = 'Naveena Pandillapally'

print(employee_1.first)
print(employee_1.fullname)
print(employee_1.email)

del employee_1.fullname
