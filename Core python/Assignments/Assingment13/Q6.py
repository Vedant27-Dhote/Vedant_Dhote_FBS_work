def multiply_values(my_dict):
    total = 1
    for value in my_dict.values():
        total = total * value
    return total


numbers = {"a": 2, "b": 3, "c": 4}
print("Multiplied Total:", multiply_values(numbers))  

