'''Use a dictionary comprehension to count the length of each word
in a sentence (take input from user)'''

s = input("Enter a string: ")
words = s.split()
word_length = {word: len(word) for word in words}
print("Length of each word:", word_length)
