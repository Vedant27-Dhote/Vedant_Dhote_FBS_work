li = [45, 34, 81, 77, 53, 34, 26, 82]
max = li[0]
for i in range(1,len(li)):
    if max<li[i]:
        max = li[i]
print(f"The maximum element is: {max}")