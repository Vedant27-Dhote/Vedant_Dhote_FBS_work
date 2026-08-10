def duplicate_list(original_list):
    new_list = []
    for num in original_list:
        new_list = new_list + [num]
    return new_list

list = [10,20,30,40]
res = duplicate_list(list)
print(res)
