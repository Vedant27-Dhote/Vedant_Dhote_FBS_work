def count_words(sentence):
    word_counts = {}
    words_list = sentence.split()
    
    for word in words_list:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
            
    return word_counts

text = "apple banana apple cherry banana apple"
print(count_words(text))

