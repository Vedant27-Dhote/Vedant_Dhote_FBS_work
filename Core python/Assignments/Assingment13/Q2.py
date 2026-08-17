'''2. Python Program to Concatenate Two Dictionaries Into One'''
def join_dictionaries(dict1, dict2):
    combined_dict = {}
    combined_dict.update(dict1)
    combined_dict.update(dict2)
    return combined_dict

boys_pets = {"dog": "Max", "fish": "Bubbles"}
girls_pets = {"cat": "Luna", "bird": "Pip"}

all_pets = join_dictionaries(boys_pets, girls_pets)


print("All pets combined:", all_pets)
