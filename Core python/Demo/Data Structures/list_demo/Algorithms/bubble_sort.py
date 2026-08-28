def Bubble_sort(list):
    size = len(list)
    for i in range(1,size):
        for j in range(0,size-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                print(list)
            else:
                continue


list = [60,100,40,20,10,30]
res = Bubble_sort(list)
print(f"Your sorted list is { list}")