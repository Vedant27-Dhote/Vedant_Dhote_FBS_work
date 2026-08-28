# Recursive Function

def series(n):
    
    if n>0:
        
        return n + series(n-1)
    else:
        return 0

n = 5                                              
res = series(n) # called the function
print(res)