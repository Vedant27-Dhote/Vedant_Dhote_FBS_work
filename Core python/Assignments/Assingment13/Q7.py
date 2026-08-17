
def remove_key(my_dict, key):
    if key in my_dict:
        my_dict.pop(key)
    return my_dict

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print("Before removal:", car)

updated_car = remove_key(car, "model")
print("After removal:", updated_car)

