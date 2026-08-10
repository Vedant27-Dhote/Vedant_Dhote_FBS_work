'''Write a program to reverse the list.'''
def reverse_list(numbers):
    reversed_list = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list = reversed_list + [numbers[i]]
    return reversed_list



list = [10,20,30,40,50]
res = reverse_list(list)
print(f"{res}")
