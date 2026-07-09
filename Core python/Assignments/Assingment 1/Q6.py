#Write a Program to input two angles from user and find third angle of the triangle.
Angle_1 = int(input("Enter Angle1:-"))
Angle_2 = int(input("Enter Angle2:-"))

Angle_3 = 180 - (Angle_1+Angle_2)  # Sum of # angles of triangle is 180

print(f"The 3rd angle is of {Angle_3} degree ")
