'''Python Program to Count the Number of Vowels in a String'''
def count(str):
    count = 0
    for i in str:
        if i== "a" or i == "A" or i == "e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
            count+=1
        else:
            continue

    return count

str = "Sohel"
res = count(str)
print(res)

        
