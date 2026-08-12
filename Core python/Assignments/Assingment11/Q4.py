''''''
def find_second_largest(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
                
    second_largest = numbers[n - 2]
    return second_largest


my_list = [10, 45, 2, 85, 34]
result = find_second_largest(my_list)
print("The second largest number is:", result)
