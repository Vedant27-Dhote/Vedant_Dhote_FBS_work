n = int(input("Enter the length for  fibnoccie series:"))
a = 0
b = 1
for i in range(n):
    print(a,end=',')
    a,b = b ,a+b
    
    
