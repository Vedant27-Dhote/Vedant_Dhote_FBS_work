def remove_intersection(set1, set2):
    set1.difference_update(set2)
    return set1

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(remove_intersection(s1, s2))
