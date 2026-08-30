def find_missing_numbers(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    
    return missing_in_set2, missing_in_set1

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
missing_2, missing_1 = find_missing_numbers(s1, s2)
print("Missing in second set:", missing_2)
print("Missing in first set:", missing_1)   
