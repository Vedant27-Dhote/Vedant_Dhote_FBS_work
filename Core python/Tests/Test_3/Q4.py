'''Write a program to print pattern
10101
01010
10101
01010
10101'''

n = 5  
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()