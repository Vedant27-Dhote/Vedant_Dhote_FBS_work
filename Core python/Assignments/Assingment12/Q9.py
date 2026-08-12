'''Python Program to Calculate the Number of Words and the Number of
Characters Present in a String'''

def count(str):
    count_char=0
    count_word=1
    for i in str:
        if i == " ":
            count_char+=0
            count_word+=1
        else:
            count_char+=1

    print(f"The number of charetcer in the string is:{count_char}")
    print(f"The number of word in the string is:{count_word}")

    

str = "My Name Is Vedant Dhote"
res = count(str)
