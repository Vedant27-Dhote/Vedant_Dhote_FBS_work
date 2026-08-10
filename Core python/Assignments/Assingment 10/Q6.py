# Remove Duplicates

def remove_duplicates(numbers):
    unique_list = []

    for num in numbers:
        already_exists = False
        for item in unique_list:
            if num == item:
                already_exists = True
                break
        
        if not already_exists:
            unique_list = unique_list + [num]
            
    return unique_list

list = [10,20,20,30,40,50,50]
res = remove_duplicates(list)
print(res)

