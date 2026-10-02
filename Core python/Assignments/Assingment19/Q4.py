''''Remove all of the vowels in a string'''
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ''.join([char for char in text if char not in vowels])
print(result)