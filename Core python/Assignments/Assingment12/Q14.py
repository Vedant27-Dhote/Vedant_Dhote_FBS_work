
def count_words(text):
    words = text.split()
    word_counts = {}
    
    for word in words:
        word = word.lower() 
        
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

user_input = input("Enter a string: ")
result_dict = count_words(user_input)

for word, count in result_dict.items():
    print(f"'{word}': {count}")
