#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
    
   
if (a + b > c) and (a + c > b) and (b + c > a):
        
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("These side lengths cannot form a valid triangle.")