#1. to pass multiple value with meaning to function 
#2. mention 2 astriks(**) symbol before parameter name in function call
#3. data stored in dictonary format
#4. use for loop on dict.items() to acess individually

def emp(**data):
    for key,val in data.items():
        print(key, ":",val)

emp(id=101, name="Vedant", age=20, add="Nagpur")