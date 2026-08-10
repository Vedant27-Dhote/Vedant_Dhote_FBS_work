'''1. Write a program to find sum of all elements of list'''
def sum(list):
    sum = 0
    for i in list:
        sum+=i

    return sum

list = [10,20,30,40,50]
res = sum(list)
print(f"The sum of all element in list is {res}")
