def search(list,Target):
    for i in range(len(list)):
        if list[i]== Target:
            return i
    else:
        return -1

Target = int(input("Enter the the number to search in th list: "))
list = [23,43,12,67,89,47,22]
res = search(list,Target)
if res != -1:
    print(f"{Target} is found at {res} index")
else:
    print(f"{Target} is not found in the list:")


