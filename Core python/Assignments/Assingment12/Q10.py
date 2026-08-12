'''Python Program to Take in Two Strings and Display the Larger String
without Using Built-in Functions'''

def large_string(str1,str2):
    count1 = 0
    count2 = 0
    for i in str1:
        count1+=1
    for i in str2:
        count2+=1

    if count1>count2:
        return str1
    elif count1<count2:
        return str2
    else:
        return -1

str1 = "Vedant"
str2 = "Vedant"
res = large_string(str1,str2)

if res == str1:
    print(f"{str1} is larger string")
elif res == str2:
    print(f"{str2} is larger string")
else:
    print("Both string are same")
    
