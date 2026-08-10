def separate_even_odd(numbers):
    even_list = []
    odd_list = []

    for num in numbers:
        if num % 2 == 0:
            even_list = even_list + [num]
        else:
            odd_list = odd_list + [num]
            
    return even_list, odd_list

list = [2,3,4,5,6,7,8]
res = separate_even_odd(list)
print(res)