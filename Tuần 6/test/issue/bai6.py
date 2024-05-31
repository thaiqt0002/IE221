import math

# Calculate the area of a circle based on the given radius.
def calc_area(radius):
    s = math.pi * radius ** 2
    return round(s, 2)