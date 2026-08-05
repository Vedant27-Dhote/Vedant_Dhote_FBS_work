n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    
    spaces = 4 * (n - i) - 2
    if spaces > 0:
        print(" " * spaces, end="")

    start = n - 1 if i == n else i
    for j in range(start, 0, -1):
        print(j, end=" " if j > 1 else "")

    print()