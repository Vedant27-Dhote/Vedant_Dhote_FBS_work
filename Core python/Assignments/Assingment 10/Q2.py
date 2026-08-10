'''2. Write a program to find maximum and minimum element in a list.'''
def max_min(list):
    n = len(list)

    for i in range(n):
        for j in range(n - i-1 ):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

list = [60,70,54,78,34]
res = max_min(list)
print(f"The max in the list is {list[len(list)-1]}")
print(f"The min in the list is {list[0]}")