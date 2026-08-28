# 1. To pass multiple values to the function
#2. mention asterisk(*) symbol before parameter name in function defination
#3. values stored in tuple format
#4. use for loop to access values individually



def add(*num):
    sum = 0
    for i in num:
        sum+=i
    print(sum)

add(10,20,30,60)