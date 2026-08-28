# To neglect positional parameter
#Assign value to parameter in function call
#Flow from right to left
#Name of parameter in fuction call and function defination should be same

def emp(id,name,sal,dept):
    data = "Id: " + str(id)+'\n'
    data += "Name: "+ str(name)+'\n'
    data += "salary: "+ str(sal)+'\n'
    data += "Department: "+ str(dept)+'\n'

    return data

res = emp(id=101, name="Vedant", sal=50000, dept="CS")
print(res)