'''Write a program to find print the following Fibonacci series using
functions:
1 1 2 3 5 8 n terms'''

def print_fibonacci(n):
    
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    a, b = 1, 1
    
    for i in range(n):
        if i == n - 1:
            print(a)  
        else:
            print(a, end=" ")
        a, b = b, a + b
terms = 6
print(f"Fibonacci series for {terms} terms:")
print_fibonacci(terms)
