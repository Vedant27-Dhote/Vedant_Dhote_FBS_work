'''Calculate the cost of painting the following building’s walls (both interior and
exterior). You need to accept area (one wall) and cost of both interior and
exterior wall.
(Note: 1. Below diagram is of two joint rooms.
2. It is upper view of building.)'''

area = float(input("Enter area of one wall: "))
number_of_walls = int(input("Enter number of walls: "))

interior_cost = float(input("Enter interior cost per sq.ft: "))
exterior_cost = float(input("Enter exterior cost per sq.ft: "))

total_area = area * number_of_walls

interior_total = total_area * interior_cost
exterior_total = total_area * exterior_cost

total_cost = interior_total + exterior_total

print("Interior painting cost =", interior_total)
print("Exterior painting cost =", exterior_total)
print("Total painting cost =", total_cost)