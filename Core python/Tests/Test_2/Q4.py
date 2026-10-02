'''Write a program to calculate the total cost of painting. The interior of building with four
equal sized walls.'''

length = float(input("Enter the length of the wall in meters: "))
height = float(input("Enter the height of the wall in meters: "))
paint_cost_per_square_meter = float(input("Enter the cost of paint per square meter: "))

wall_area = length * height
total_area = 4 * wall_area
total_cost = total_area * paint_cost_per_square_meter

print(f"Total cost of painting the building: Rs. {total_cost}")
