def checkpalindrome(num):
    temp = num
    rev = 0
    while temp>0:
        d = temp%10
        rev = rev*10+d
        temp//=10

    if(num==rev):
        return True
    else:
        return False

data = [121,453,676,890]

x = list(map(checkpalindrome,data))
print(x)