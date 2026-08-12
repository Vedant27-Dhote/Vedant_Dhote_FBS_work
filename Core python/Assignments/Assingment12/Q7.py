'''Python Program to Calculate the Length of a String Without Using a
Library Function'''

def length(str):
    count = 0
    for i in str:
        count+=1

    return count

print(length("Vedant"))
