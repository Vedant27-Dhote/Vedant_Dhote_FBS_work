'''Python Program to Form a New String where the First Character and
the Last Character have been Exchanged'''

def exchange(str):
    
    lastAlphabet = str[len(str)-1]
    FirstElement = str[0]
    c = ""
    for i in range(1,len(str)-1):
        c+=str[i]
    return lastAlphabet+c+FirstElement
    

res = exchange("Vedant")
print(res)