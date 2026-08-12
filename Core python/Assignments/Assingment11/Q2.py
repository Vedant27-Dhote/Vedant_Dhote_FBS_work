'''Python Program to Merge Two Lists and Sort it'''

def merge_list(li1,li2):
    for i in li2:
        li1.append(i)
    n = len(li1)
    for i in range(n):
        for j in range(n - i-1 ):
            if li1[j] > li1[j + 1]:
                li1[j], li1[j + 1] = li1[j + 1], li1[j]

    return li1

    

list = [1,2,34,5,6,7,8,9]
list2 = [12,34,5,53]
res = merge_list(list,list2)
print(res)