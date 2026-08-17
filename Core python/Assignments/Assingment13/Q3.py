
def check_key(my_dict, key):
    if key in my_dict:
        return True
    else:
        return False

fruits = {"apple": 5, "banana": 3, "orange": 2}

print(check_key(fruits, "apple"))

print(check_key(fruits, "grape"))
