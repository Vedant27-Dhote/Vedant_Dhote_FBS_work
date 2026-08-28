'''def is_anagram(str1):
    dict = {}
    count = 1
    for i in str1:
        if i in dict:
            count+=1
        dict.update({i:count})

    return dict
str = "aabcda"
str2 = "baacad"
res = is_anagram(str)
print(res)''' # error