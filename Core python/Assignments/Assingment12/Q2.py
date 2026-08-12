'''Python Program to Remove the nth Index Character from a Non-Empty
String'''

def n_index(str,index):
    new_str=""
    for i in range(len(str)):
        if i!=index:
            new_str+=str[i]
        else:
            continue
    return new_str


str = "Vedant"
res = n_index(str,2)
print(res)
            