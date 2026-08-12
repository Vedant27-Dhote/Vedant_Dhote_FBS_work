
def find_intersection(list1, list2):
    intersection_result = []
    
    for item in list1:
        if item in list2:
            if item not in intersection_result:
                intersection_result.append(item)
                
    return intersection_result


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = find_intersection(a, b)
print("Intersection of lists:", result)
