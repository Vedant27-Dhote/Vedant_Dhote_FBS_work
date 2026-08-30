def elements_not_in_second(set1, set2):
    return set1.difference(set2)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(elements_not_in_second(s1, s2))  
