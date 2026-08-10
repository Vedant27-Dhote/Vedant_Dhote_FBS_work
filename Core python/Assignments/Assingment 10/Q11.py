def find_divisible(numbers, m, n):
    divisible_list = []
    for num in numbers:
        if num % m == 0 and num % n == 0:
            divisible_list = divisible_list + [num]
    return divisible_list


list = [10, 15, 20, 30, 40, 60]
print(find_divisible(list, 3, 5))
