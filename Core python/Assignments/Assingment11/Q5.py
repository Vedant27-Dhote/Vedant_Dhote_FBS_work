
def sort_by_length(word_list):
    n = len(word_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(word_list[j]) > len(word_list[j + 1]):
                temp = word_list[j]
                word_list[j] = word_list[j + 1]
                word_list[j + 1] = temp
    return word_list

my_words = ["apple", "pie", "banana", "kiwi"]
result = sort_by_length(my_words)
print("Sorted by length:", result)
