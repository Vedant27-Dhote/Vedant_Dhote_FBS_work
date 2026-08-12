'''Python Program to Put Even and Odd elements of a List into two Different
Lists'''

def even_odd(list):
    Odd_list = []
    even_list = []
    for i in list:
        if i%2==0:
            even_list.append(i)
        else:
            Odd_list.append(i)
    return even_list, Odd_list

list = [1,2,34,5,6,7,8,9]
res = even_odd(list)
print(res)