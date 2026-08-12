'''Python Program to Remove the Characters of Odd Index Values in a
String'''

def odd(str):
    new_str =""
    for i in range(len(str)):
        if i%2==0:
            new_str+=str[i]
        else:
            continue
    return new_str

print(odd("Vedant"))