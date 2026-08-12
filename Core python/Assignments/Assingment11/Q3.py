'''Python Program to Sort the List According to the Second Element in Sublist'''

def sort_by_second_element(main_list):
    n = len(main_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if main_list[j][1] > main_list[j + 1][1]:
                temp = main_list[j]
                main_list[j] = main_list[j + 1]
                main_list[j + 1] = temp
    return main_list


my_list = [[1, 5], [2, 1], [3, 9], [4, 3]]
result = sort_by_second_element(my_list)
print("Sorted list:", result)
