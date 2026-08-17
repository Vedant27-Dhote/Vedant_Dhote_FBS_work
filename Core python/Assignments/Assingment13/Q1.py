'''1. Python Program to Add a Key-Value Pair to the Dictionary'''

def add(dict, key, value):
    dict[key] = value
    return dict

dict = {
    "Name": "Vedant",
    "id" : 101
}
res = add(dict,"Salary",500000)

print(res)
