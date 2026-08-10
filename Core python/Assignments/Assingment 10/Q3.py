'''3. Write a program to find the second largest element in the list.'''
def find_second_largest(numbers):
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num < largest:
            if second_largest is None or num > second_largest:
                second_largest = num
                
    return second_largest

list = [10,20,30,40,50]
res = find_second_largest(list)
print(res)
