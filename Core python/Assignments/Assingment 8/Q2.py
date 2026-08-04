'''Write a program to calculate area of circle'''
import math
def Area(r):
    return 2*math.pi*r

r = int(input("Enter the Radius of circle:"))
res = Area(r)
print(res)