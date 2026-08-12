'''Python Program to replace every blank space with hyphen in a string.'''
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

