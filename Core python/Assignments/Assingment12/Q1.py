'''Python Program to Replace all Occurrences of a with $ in a String'''
def replace(str):
    new_str=""
    for i in str:
        if i=="a":
            new_str+="$"
        else:
            new_str+=i
    return new_str

str = "Vedant"
res = replace(str)
print(res)
            
