'''Count the number of spaces in a string using comprehension'''
text = "Hello, how are you?"
space_count = len([char for char in text if char == ' '])
print(space_count)
