'''There is a list with some numbers. Create a new
dictionary using this list in such a way that key is
number and value is frequency of occurrence of that
number in list.

[1,3,4,1,2,3,6,7,1,2,4]
{1:3,3:2,2:2,'''

numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
