#.Write a program to calculate area of an equilateral triangle.
side = float(input("Enter the side of the equilateral triangle: "))


sqrt_3 = 3 ** 0.5

area = (sqrt_3 / 4) * (side ** 2)


print(f"Area of the equilateral triangle: {area}")