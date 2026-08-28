# 1.Structure : denoted by []
li = [10, 20, 30, 40]
print(type(li))

# 2.type of data: heterogenus
li = [10, 3.14, "abc"]
print(li)

# 3.sequence : ordered

# 4.changable: mutable
print(id(li))
li[2] = 4
print (id(li))
print(li)

# 5. duplication: Allowed

li = [1, 2, 3, 4, 1 ,1]
print(li)

list = ["Vedant","Dhote"]
str = ''.join(list)
print(str)

print(str.split('e'))

str = "Vedant Dhote 123"
print(str.strip(" "))