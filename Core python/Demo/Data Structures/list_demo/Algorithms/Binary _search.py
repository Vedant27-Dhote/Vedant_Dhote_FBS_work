def Binary(list,Target):
    beg = 0
    end = len(list)-1
    while beg<=end:
        mid = (beg+end)//2
        if list[mid]==Target:
            return mid
        elif list[mid]<Target:
            beg = mid+1
        else:
            end = mid -1
    else:
        return -1

list = [10,20,30,40,50,60]
Target = int(input("Enter the number to find in the list:"))
res = Binary(list,Target)

if res!=-1:
    print(f"The {Target} is found at index {res}")
else:
    print(f"The element is not found in the list")