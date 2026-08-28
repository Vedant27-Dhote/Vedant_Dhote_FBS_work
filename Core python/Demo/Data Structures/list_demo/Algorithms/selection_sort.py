def Selection_sort(list):
    size=len(list)
    for i in range(0,size-1):
        min = i
        for j in range(i+1,size):
            if (list[j]<list[min]):
                min = j

        list[i], list[min]=list[min],list[i]
        print(list)

    



list = [40,10,60,30,50,20]
Selection_sort(list)
print(f"Your sorted list is {list}")