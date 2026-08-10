def remove_all_occurrences(numbers, to_remove):
    filtered_list = []
    for num in numbers:
        if num != to_remove:
            filtered_list = filtered_list + [num]
    return filtered_list

list = [2,3,4,5,6,2,7,8]
res = remove_all_occurrences(list,2)
print(res)