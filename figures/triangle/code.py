from math import sqrt
a = 7
b = 2
c = 8

def triangle_perimeter(storona1 = a, storona2 = b, storona3 = c):
    return storona1 + storona2 + storona3

def triangle_area(storona1 = a, storona2 = b, storona3 = c):
    p = (storona1 + storona2 + storona3) / 2
    return sqrt(p * (p - storona1) * (p - storona2) * (p - storona3))