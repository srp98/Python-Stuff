"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, x):
        self.items.append(x)

    def getClassiness(self):
        score = 0
        if len(self.items) > 0:
            for i in self.items:
                if i == 'tophat':
                    score += 2
                if i == 'bowtie':
                    score += 4
                if i == 'monocle':
                    score += 5
        return score


# Test cases
me = Classy()
print(me.getClassiness())  # Should be 0

me.addItem("tophat")

print(me.getClassiness())  # Should be 2

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")

print(me.getClassiness())  # Should be 11

me.addItem("bowtie")
print(me.getClassiness())  # Should be 15
