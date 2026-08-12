
def get_length(text):
    count = 0
    for char in text:
        count += 1
    return count


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


len1 = get_length(string1)
len2 = get_length(string2)

if len1 > len2:
    print(f"The larger string is: '{string1}'")
elif len2 > len1:
    print(f"The larger string is: '{string2}'")
else:
    print("Both strings are equal in length.")
