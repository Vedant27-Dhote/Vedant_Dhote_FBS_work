'''Sum of all odd numbers between 1 to n'''
def Sum(n):
    sum = 0
    for i in range(1,n):
        if i%2!=0:
            sum+=i
    return sum

n = int(input("Enter the number till which you want odd numbers:"))
res = Sum(n)
print(res)