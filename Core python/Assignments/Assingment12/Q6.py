'''Python Program to Take in a String and Replace Every Blank Space
with Hyphen'''

def replace(str):
    new_str = ""
    for i in str:
        if i==" ":
            new_str+="-"
        else:
            new_str+=i

    return new_str

str = "Vedant Dhote"
res = replace(str)
print(res)


