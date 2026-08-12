'''Anagram strings'''

def is_anagram(str1,str2):
    if len(str1)==len(str2):
        for i in str1:
            if i not in str2:
                return -1
        return True
    else:
        return False

str1 = input("Enter string 1:")
str2 = input("Enter string 2:")
res = is_anagram(str1,str2)

if res == True:
    print("The given strings are anagram")
else:
    print("The string is not anagram")