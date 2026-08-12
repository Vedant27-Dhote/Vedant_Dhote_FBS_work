'''Python Program to count number of lowercase characters in a string.'''

def count_lowercase(text):
    lowercase_count = 0
    
    for char in text:
        if char.islower():
            lowercase_count += 1
            
    return lowercase_count

str = "Vedant"
result = count_lowercase(str)
print(f"Number of lowercase characters: {result}")


