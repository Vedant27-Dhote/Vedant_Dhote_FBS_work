
def find_union(list1, list2):
    union_result = []
    
    for item in list1:
        if item not in union_result:
            union_result.append(item)
            
    for item in list2:
        if item not in union_result:
            union_result.append(item)
            
    return union_result

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = find_union(a, b)
print("Union of lists:", result)
