'''A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
cost of fencing the field.'''


radius = 20
length = 50
breadth = 40
wire_cost_per_meter = 35
fencing_iterations = 5

circular_perimeter = 2 * 3.14 * radius
rectangular_perimeter = 2 * (length + breadth)

total_fencing_length = circular_perimeter + rectangular_perimeter
total_fencing_length *= fencing_iterations


total_cost = total_fencing_length * wire_cost_per_meter
print(f"Total cost of fencing the field: Rs. {total_cost}")
