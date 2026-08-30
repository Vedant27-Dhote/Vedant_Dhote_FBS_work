def word_frequency(list_of_strings):
    all_words = " ".join(list_of_strings).split()
    unique_words = set(all_words)
    
    counts = {}
    for word in unique_words:
        counts[word] = all_words.count(word)
        
    return counts

strings = ["hello world", "hello Python", "world of Python"]
print(word_frequency(strings))  
