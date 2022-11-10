import math


def compute_area(r):
    return math.pi * r * r
radius = float(input("What is the radius:" ))

print(f"the area is {compute_area(radius)}")