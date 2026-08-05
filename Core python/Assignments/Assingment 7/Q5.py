n = 5

for i in range(1, n + 1):
    print(" " * (n - i) * 2, end="")
    
    for j in range(1, i + 1):
        if j == 1 or i == n:
            print(j, end=" ")
        elif j == i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
            
    for j in range(1, i - 1):
        if i == n:
            print(j + 2, end=" ")
        else:
            print(" ", end=" ")
            
    if i > 1 and i < n:
        print(1, end="")
        
    print()
