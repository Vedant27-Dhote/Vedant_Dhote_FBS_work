'''Python Program to Generate a Dictionary that Contains Numbers (between 1
and n) in the Form (x,x*x).'''

def square_dictionary(n):
    result = {}
    for x in range(1, n + 1):
        result[x] = x * x
    return result


print(square_dictionary(5))  

