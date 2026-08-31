'''Python Program to Find the Union of two Lists without
using set concept.'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for item in list2:
    if item not in list1:
        list1.append(item)

print(list1)
