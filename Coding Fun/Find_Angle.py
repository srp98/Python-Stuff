"""
Program to find the angle <MBC of a triangle ABC, where
- AB and BC are sides of triangle
- AC is hypotenuse and
- M is the mid point of AC
"""
import math

AB, BC = int(input()), int(input())
hype = math.hypot(AB, BC)
res = round(math.degrees(math.acos(BC/hype)))
degree = chr(176)
print(res, degree, sep='')
