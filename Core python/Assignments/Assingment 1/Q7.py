#Program to Find the Roots of a Quadratic Equation

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

x = (b**2) - (4*a*c)


sqrt = x ** 0.5

root1 = (-b + sqrt) / (2*a)
root2 = (-b - sqrt) / (2*a)

print(f"Root 1: {root1}")
print(f"Root 2: {root2}")

